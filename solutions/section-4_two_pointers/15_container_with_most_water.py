"""
## Problem 15 — Container With Most Water

  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
"""


def solution(height: list[int]) -> int:
    if not height or len(height) <= 1:
        return 0

    left = 0
    right = len(height) - 1

    max_vol = 0

    while left < right:
        x = right - left
        y = min(height[right], height[left])
        vol = x * y
        max_vol = max(max_vol, vol)

        if y == height[right]:
            right -= 1
        else:
            left += 1

    return max_vol


def main():
    height = [1, 4, 3, 7, 5, 4, 8, 2]
    result = solution(height)

    print(result)


if __name__ == "__main__":
    main()
