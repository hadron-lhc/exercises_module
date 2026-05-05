"""
## Problem 18 — Count Events per User

  Input:
  events = ["u1","u2","u1"]

  Output:
  {"u1":2,"u2":1}
"""

from collections import defaultdict


def solution(events: list[str]) -> dict:
    result = defaultdict(int)
    for event in events:
        result[event] += 1

    return dict(result)


def main():
    events = ["u1", "u2", "u1"]

    result = solution(events)
    print(result)


if __name__ == "__main__":
    main()
