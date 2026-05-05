"""
## Problem 14 — Two Sum II (Sorted)

  Input: nums = [2,7,11,15], target = 9
  Output: [1,2]
"""


def solution(nums: list[int], target: int) -> list[int]:
    if not nums or not target:
        return []

    left = 0
    right = len(nums) - 1
    current_sum = nums[left] + nums[right]

    while left < right:
        while current_sum > target:
            right -= 1
            current_sum = nums[left] + nums[right]
        while current_sum < target:
            left += 1
            current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1, right + 1]

    return []


def main():
    nums = [2, 7, 11, 15]
    target = 17

    result = solution(nums, target)
    print(result)


if __name__ == "__main__":
    main()
