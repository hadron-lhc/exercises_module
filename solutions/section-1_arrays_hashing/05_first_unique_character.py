"""
## Problem 5 — First Unique Character

Description Return the first non-repeating character.

Example

  Input: s = "leetcode"
  Output: "l"
"""

from collections import Counter


def solution(s: str) -> str:
    count_freq = Counter(s)

    if s == "":
        return ""

    for char in s:
        if count_freq[char] == 1:
            return char

    return ""


def main():
    s = "leetcode"
    result = solution(s)

    print(result)


if __name__ == "__main__":
    main()
