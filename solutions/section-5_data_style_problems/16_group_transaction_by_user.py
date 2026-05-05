"""
## Problem 16 — Group Transactions by User

  Input:
  [("user1",100), ("user2",50), ("user1",200)]

  Output:
  {
    "user1": [100,200],
    "user2": [50]
  }
"""

from collections import defaultdict


def solution(users):
    result = defaultdict(list)

    for user, amount in users:
        result[user].append(amount)

    return dict(result)


def main():
    users = [("user1", 100), ("user2", 50), ("user1", 200)]

    result = solution(users)
    print(result)


if __name__ == "__main__":
    main()
