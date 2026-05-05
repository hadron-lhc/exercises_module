"""
## Problem 20 — Meeting Rooms

  Input: [[0,30],[5,10],[15,20]]
  Output: false
"""


def solution(schedules: list[list[int]]) -> bool:
    prev_schedule = [schedules[0]]

    for i in range(1, len(schedules)):
        if schedules[i][0] < prev_schedule[-1][1]:
            return False
        else:
            prev_schedule.append(schedules[i])

    return True


def main():
    schedules = [[0, 30], [5, 10], [15, 20]]

    result = solution(schedules)
    print(result)


if __name__ == "__main__":
    main()
