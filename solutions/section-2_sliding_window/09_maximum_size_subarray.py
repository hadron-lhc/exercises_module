"""
## Problem 9 — Maximum Average Subarray (Fixed Window)

  Input: nums = [1,12,-5,-6,50,3], k = 4
  Output: 12.75
"""


def solution(nums: list[int], k: int) -> float:
    left = 0
    window = nums[left:k]
    current_sum = sum(window)
    max_average = current_sum / k

    for right in range(k, len(nums)):
        current_sum += nums[right]
        current_sum -= nums[left]
        max_average = max(max_average, current_sum / k)
        left += 1
        right += 1

    return max_average


def main():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    result = solution(nums, k)
    print(result)


if __name__ == "__main__":
    main()
