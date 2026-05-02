"""
## Problem 4 — Valid Anagram

Description Return true if  t  is an anagram of  s .

Example

  Input: s = "listen", t = "silent"
  Output: true
"""

from collections import Counter


def solution(s: str, t: str) -> bool:
    counter_s = Counter(s)
    counter_t = Counter(t)

    return counter_s == counter_t


def main():
    s = "listen"
    t = "silent"

    result = solution(s, t)
    print(result)  # True


if __name__ == "__main__":
    main()
