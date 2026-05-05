"""
## Problem 11 — Running Sum

  Input: nums = [1,2,3,4]
  Output: [1,3,6,10]
"""


def solution(nums: list[int]) -> list[int]:
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]

    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    return prefix_sum


def main():
    nums = [1, 2, 3, 4]
    result = solution(nums)

    print(result)


if __name__ == "__main__":
    main()
