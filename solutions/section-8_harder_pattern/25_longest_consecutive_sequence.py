"""
## Problem 25 — Longest Consecutive Sequence

  Input: [100,4,200,1,3,2]
  Output: 4
"""


def solution(nums: list[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    input = [100, 4, 200, 1, 3, 2]
    result = solution(input)

    print(result)  # OUTPUT: 4


if __name__ == "__main__":
    main()
