"""
## Problem 22 — Reactivated Users

  Definition:
  gap >= 30 days between orders

  Output:
  month | reactivated_users
"""

import sqlite3


def solution(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
    query = """
        WITH base AS (
            SELECT *,
                   LAG(order_date) OVER (
                        PARTITION BY user_id
                        ORDER BY order_date
                   ) AS prev_order
            FROM orders
        ),
        groups AS (
            SELECT *,
                   CASE
                        WHEN (julianday(order_date) - julianday(prev_order)) >= 30 THEN 1
                        ELSE 0
                    END AS reactivated_condition
            FROM base
        )
        SELECT
            strftime('%Y-%m', order_date) AS month,
            COUNT(*) AS reactivated_users
        FROM groups
        WHERE reactivated_condition = 1
        GROUP BY month
        ORDER BY month
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def main():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("CREATE TABLE orders (user_id INTEGER, order_date TEXT)")

    # Insert sample data
    cursor.executemany(
        "INSERT INTO orders (user_id, order_date) VALUES (?, ?)",
        [
            (1, "2023-01-01"),
            (2, "2023-01-15"),
            (3, "2023-02-01"),
            (4, "2023-03-01"),
            (1, "2023-03-15"),
            (2, "2023-03-20"),
            (3, "2023-04-01"),
            (5, "2023-04-01"),
            (6, "2023-05-01"),
            (5, "2027-05-05"),
        ],
    )

    result = solution(conn)
    print(result)


if __name__ == "__main__":
    main()
