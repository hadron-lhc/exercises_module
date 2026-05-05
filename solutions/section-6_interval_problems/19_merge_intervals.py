"""
## Problem 19 — Merge Intervals

  Input: [[1,3],[2,6],[8,10]]
  Output: [[1,6],[8,10]]
"""


def solution(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        last_merged_start, last_merged_end = merged[-1]

        if current_start <= last_merged_end:
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            merged.append([current_start, current_end])

    return merged


def main():
    intervals = [[1, 3], [2, 6], [8, 10]]
    result = solution(intervals)
    print(result)  # Output: [[1, 6], [8, 10]]


if __name__ == "__main__":
    main()
