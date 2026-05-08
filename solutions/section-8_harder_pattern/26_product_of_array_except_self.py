"""
## Problem 26 — Product of Array Except Self

  Input: [1,2,3,4]
  Output: [24,12,8,6]
"""


def solution(nums: list[int]) -> list[int]:
    """
    [1, 1, 2, 6]
    [1, 4, 12, 24]

    [24*1, 12*1, 4*2, 1*6]

    [24, 12, 8, 6]
    """

    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


def main():
    input = [1, 2, 3, 4]
    result = solution(input)

    print(result)  # Output: [24,12,8,6]


if __name__ == "__main__":
    main()
