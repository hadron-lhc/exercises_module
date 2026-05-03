"""
## Problem 6 — Longest Substring Without Repeating Characters

  Input: s = "abcabcbb"
  Output: 3
"""


def solution(s: str) -> int:
    left = 0
    max_len = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        max_len = max(max_len, right - left + 1)
        seen.add(s[right])

    return max_len


def main():
    s = "abdabbaberfabc"
    result = solution(s)

    print(result)


if __name__ == "__main__":
    main()
