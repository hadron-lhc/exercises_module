"""
## Problem 17 — Merge Users and Orders

  Input:
  users = [{id:1,name:"Ana"}]
  orders = [{id:1,amount:100}]

  Output:
  [{id:1,name:"Ana",orders:[100]}]
"""


def solution(users, orders):
    orders_map = {}
    for o in orders:
        user_id = o["id"]
        if user_id not in orders_map:
            orders_map[user_id] = []
        orders_map[user_id].append(o["amount"])

    result = []
    for user in users:
        user_id = user["id"]
        merged_user = {
            "id": user_id,
            "name": user["name"],
            "orders": orders_map.get(user_id, []),
        }
        result.append(merged_user)

    return result


def main():
    users = [{"id": 1, "name": "Ana"}]
    orders = [{"id": 1, "amount": 100}]

    result = solution(users, orders)
    print(result)


if __name__ == "__main__":
    main()
