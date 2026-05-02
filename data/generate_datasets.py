import pandas as pd


def create_datasets():
    # Users
    users = pd.DataFrame(
        [
            {"user_id": 1, "signup_date": "2024-01-01"},
            {"user_id": 2, "signup_date": "2024-01-02"},
            {"user_id": 3, "signup_date": "2024-01-05"},
            {"user_id": 4, "signup_date": "2024-01-10"},
        ]
    )
    users["signup_date"] = pd.to_datetime(users["signup_date"])

    # Orders
    orders = pd.DataFrame(
        [
            {"user_id": 1, "order_date": "2024-01-01", "amount": 100},
            {"user_id": 1, "order_date": "2024-01-03", "amount": 50},
            {"user_id": 1, "order_date": "2024-02-10", "amount": 200},
            {"user_id": 2, "order_date": "2024-01-02", "amount": 80},
            {"user_id": 2, "order_date": "2024-03-05", "amount": 120},
            {"user_id": 3, "order_date": "2024-01-10", "amount": 60},
            {"user_id": 4, "order_date": "2024-01-15", "amount": 200},
            {"user_id": 4, "order_date": "2024-01-16", "amount": 150},
        ]
    )
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    # Events
    events = pd.DataFrame(
        [
            {"user_id": 1, "event_time": "2024-01-01 10:00:00"},
            {"user_id": 1, "event_time": "2024-01-01 10:10:00"},
            {"user_id": 1, "event_time": "2024-01-01 11:00:00"},
            {"user_id": 2, "event_time": "2024-01-02 09:00:00"},
            {"user_id": 2, "event_time": "2024-01-02 09:20:00"},
            {"user_id": 2, "event_time": "2024-01-02 10:00:00"},
            {"user_id": 3, "event_time": "2024-01-03 15:00:00"},
        ]
    )
    events["event_time"] = pd.to_datetime(events["event_time"])

    # Transactions (Python-style)
    transactions = [
        ("user1", 100),
        ("user2", 50),
        ("user1", 200),
        ("user3", 300),
    ]

    return users, orders, events, transactions


if __name__ == "__main__":
    users, orders, events, transactions = create_datasets()

    print("Users:\n", users, "\n")
    print("Orders:\n", orders, "\n")
    print("Events:\n", events, "\n")
    print("Transactions:\n", transactions)
