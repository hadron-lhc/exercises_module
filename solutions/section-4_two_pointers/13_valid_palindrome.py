"""
## Problem 13 — Valid Palindrome

  Input: s = "A man, a plan, a canal: Panama"
  Output: true
"""


def solution(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def main():
    s = "A man, a plan, a canal: Panama"
    result = solution(s)

    print(result)


if __name__ == "__main__":
    main()
