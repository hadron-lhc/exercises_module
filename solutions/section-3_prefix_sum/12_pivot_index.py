"""
## Problem 12 — Pivot Index

  Input: nums = [1,7,3,6,5,6]
  Output: 3
"""


def solution(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0

    for i, x in enumerate(nums):
        if left_sum == (total - left_sum - x):
            return i
        left_sum += x

    return -1


def main():
    nums = [1, 7, 3, 6, 5, 6]
    result = solution(nums)

    print(result)


if __name__ == "__main__":
    main()
