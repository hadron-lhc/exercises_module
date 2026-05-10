"""
## Problem 27 — Gas Station

  Input:
  gas = [1,2,3,4,5]
  cost = [3,4,5,1,2]

  Output: 3
"""


def solution(gas: list[int], cost: list[int]) -> int:
    total_gas = 0
    total_cost = 0
    len_road = len(gas)

    for i in range(len_road):
        total_gas += gas[i]
        total_cost += cost[i]

    if total_cost > total_gas:
        return -1

    start_index = 0
    current_gas = 0
    for i in range(len_road):
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            start_index = i + 1
            current_gas = 0

    return start_index


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [4, 5, 1, 2, 3]

    result = solution(gas, cost)
    print(result)


if __name__ == "__main__":
    main()
