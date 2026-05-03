"""
## Problem 7 — Longest Substring with At Most K Distinct Characters

  Input: s = "eceba", k = 2
  Output: 3
"""


def solution(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    s = "eceba"
    k = 2

    result = solution(s, k)
    print(result)


if __name__ == "__main__":
    main()
