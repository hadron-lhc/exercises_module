"""
## Problem 3 — Top K Frequent Elements
Description Return the  k  most frequent elements.

Example

  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]
"""

from collections import Counter


def solution(nums: list[int], k: int) -> list[int]:
    count_freq = Counter(nums)
    top_k = count_freq.most_common(k)

    return [i for i, _ in top_k]


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    result = solution(nums, k)
    print(result)


if __name__ == "__main__":
    main()
