SELECT * FROM Customers;
INSERT INTO Accounts (customer_id, account_type, balance)
VALUES (1, 'SAVINGS', 1000.00);
SELECT * FROM Accounts WHERE account_id = 1;
UPDATE Accounts SET balance = balance + 500.00 WHERE account_id = 1;
INSERT INTO Transactions (account_id, transaction_type, amount, date)
VALUES (1, 'DEPOSIT', 500.00, NOW());
UPDATE Accounts SET balance = balance - 200.00 WHERE account_id = 1;
INSERT INTO Transactions (account_id, transaction_type, amount, date)
VALUES (1, 'WITHDRAWAL', 200.00

