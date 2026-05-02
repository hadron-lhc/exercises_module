"""
## Problem 1 — Contains Duplicate

Description Given an integer array  nums , return  true  if any value
appears at least twice.

Example

  Input: nums = [1,2,3,1]
  Output: true

  Input: nums = [1,2,3,4]
  Output: false
"""

from collections import Counter


def solution(nums: list[int]) -> bool:
    counter_freq = Counter(nums)
    return any(k != 1 for k in counter_freq.values())


def main():
    nums = [1, 2, 3, 4]
    result = solution(nums)

    print(result)


if __name__ == "__main__":
    main()
