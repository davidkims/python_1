CREATE TABLE Customers (
  customer_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(50) NOT NULL,
  address VARCHAR(100) NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE Accounts (
  account_id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL,
  account_type VARCHAR(20) NOT NULL,
  balance DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (account_id),
  FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
);

CREATE TABLE Transactions (
  transaction_id INT NOT NULL AUTO_INCREMENT,
  account_id INT NOT NULL,
  transaction_type VARCHAR(20) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  date DATE NOT NULL,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (account_id) REFERENCES Accounts (account_id)
);
