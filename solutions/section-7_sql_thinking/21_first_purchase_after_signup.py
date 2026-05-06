"""
## Problem 21 — First Purchase After Signup

  users:
  id | signup_date

  orders:
  id | order_date

  Output:
  first order after signup per user

"""

import sqlite3


def solution(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
    query = """
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def main():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, signup_date TEXT)")
    cursor.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, order_date TEXT)")

    # Insert sample data
    cursor.executemany(
        "INSERT INTO users (id, signup_date) VALUES (?, ?)",
        [(1, "2024-01-01"), (2, "2024-01-02"), (3, "2024-01-03")],
    )
    cursor.executemany(
        "INSERT INTO orders (id, order_date) VALUES (?, ?)",
        [(1, "2024-01-02"), (2, "2024-01-03"), (3, "2024-01-04"), (4, "2024-01-05")],
    )

    result = solution(conn)
    print(result)


if __name__ == "__main__":
    main()
