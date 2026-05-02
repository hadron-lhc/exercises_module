"""
## Problem 2 — Two Sum

Description Return indices of the two numbers such that they add up to
target.

Example

  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
"""


def solution(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9

    result = solution(nums, target)
    print(result)


if __name__ == "__main__":
    main()
