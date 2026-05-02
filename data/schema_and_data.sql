-- DROP TABLES (optional)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS events;

-- USERS
CREATE TABLE users (
    user_id INT,
    signup_date DATE
);

INSERT INTO users (user_id, signup_date) VALUES
(1, '2024-01-01'),
(2, '2024-01-02'),
(3, '2024-01-05'),
(4, '2024-01-10');

-- ORDERS
CREATE TABLE orders (
    user_id INT,
    order_date DATE,
    amount INT
);

INSERT INTO orders (user_id, order_date, amount) VALUES
(1, '2024-01-01', 100),
(1, '2024-01-03', 50),
(1, '2024-02-10', 200),
(2, '2024-01-02', 80),
(2, '2024-03-05', 120),
(3, '2024-01-10', 60),
(4, '2024-01-15', 200),
(4, '2024-01-16', 150);

-- EVENTS
CREATE TABLE events (
    user_id INT,
    event_time TIMESTAMP
);

INSERT INTO events (user_id, event_time) VALUES
(1, '2024-01-01 10:00:00'),
(1, '2024-01-01 10:10:00'),
(1, '2024-01-01 11:00:00'),
(2, '2024-01-02 09:00:00'),
(2, '2024-01-02 09:20:00'),
(2, '2024-01-02 10:00:00'),
(3, '2024-01-03 15:00:00');
