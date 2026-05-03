"""
## Problem 8 — Minimum Size Subarray Sum

  Input: nums = [2,3,1,2,4,3], target = 7
  Output: 2
"""


def solution(nums: list[int], target: int) -> int:
    left = 1
    current_sum = 0
    min_long = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_long = min(min_long, right - left + 1)
            current_sum -= nums[left]
            left += 1

    if min_long == float("inf"):
        return 0
    else:
        return min_long


def main():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    result = solution(nums, target)
    print(result)


if __name__ == "__main__":
    main()
