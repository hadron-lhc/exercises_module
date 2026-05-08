"""
## Problem 23 — Sessionization

  Definition:
  new session if gap > 30 min

  Output:
  user_id | session_id | events_count
"""

import sqlite3


def solution(conn):
    query = """
        WITH base as (
            SELECT
                *,
                LAG(event_time) OVER (
                    PARTITION BY user_id
                    ORDER BY event_time
                )AS prev_event
            FROM events
        ),
        flags AS (
            SELECT
                *,
                CASE
                    WHEN prev_event IS NULL THEN 1
                    WHEN (julianday(event_time) - julianday(prev_event))*1440 > 30 THEN 1
                    ELSE 0
                END AS flag_newsession
            FROM base
        ),
        sessions AS (
            SELECT
                *,
                SUM(flag_newsession) OVER (
                    PARTITION BY user_id
                    ORDER BY event_time
                ) AS session_id
            FROM flags
        )
        SELECT
            user_id,
            session_id,
            COUNT(*) AS count_users
        FROM
            sessions
        GROUP BY
            user_id,
            session_id
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def cargar_datos(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE events (
            user_id INTEGER,
            event_time TIMESTAMP
        )
    """)
    # Insertar datos de ejemplo
    cursor.executemany(
        """
        INSERT INTO events (user_id, event_time) VALUES (?, ?)
    """,
        [
            (1, "2024-01-01 10:00:00"),
            (1, "2024-01-01 10:20:00"),
            (1, "2024-01-01 11:00:00"),
            (2, "2024-01-01 10:05:00"),
            (2, "2024-01-01 10:40:00"),
            (2, "2024-01-01 11:30:00"),
        ],
    )
    conn.commit()


def main():
    conn = sqlite3.connect(":memory:")
    cargar_datos(conn)

    result = solution(conn)
    print(result)


if __name__ == "__main__":
    main()
