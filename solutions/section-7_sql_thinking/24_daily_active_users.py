"""
## Problem 24 — Daily Active Users (DAU)

  Input:
  events(user_id, date)

  Output:
  date | unique_users
"""

import sqlite3


def solution(conn):
    query = """
        WITH base AS (
            SELECT
                *,
                strftime('%d/%m', date) AS day
            FROM events
        )
        SELECT
            date,
            COUNT((SELECT DISTINCT user_id)) AS unique_users
        FROM
            base
        GROUP BY day
    """

    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def create_data(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE events (
            user_id INTEGER,
            date TIMESTAMP
        )
    """)
    # Insertar datos de ejemplo
    cursor.executemany(
        """
        INSERT INTO events (user_id, date) VALUES (?, ?)
    """,
        [
            (1, "2024-01-01"),
            (2, "2024-01-01"),
            (1, "2024-01-02"),
            (3, "2024-01-02"),
            (2, "2024-01-03"),
        ],
    )
    conn.commit()


def main():
    conn = sqlite3.connect(":memory:")
    create_data(conn)

    result = solution(conn)
    print(result)


if __name__ == "__main__":
    main()
