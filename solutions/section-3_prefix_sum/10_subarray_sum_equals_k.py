"""
## Problem 10 — Subarray Sum Equals K

  Input: nums = [1,1,1], k = 2
  Output: 2
"""


def solution(nums: list[int], k: int) -> int:
    count = 0
    current_sum = 0
    sums_dict = {0: 1}

    for n in nums:
        current_sum += n
        diff = current_sum - k

        if diff in sums_dict:
            count += sums_dict[diff]

        sums_dict[current_sum] = sums_dict.get(current_sum, 0) + 1

    return count


def main():
    nums = [1, 1, 1]
    k = 2

    result = solution(nums, k)
    print(result)


if __name__ == "__main__":
    main()
