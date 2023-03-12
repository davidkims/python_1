import mysql.connector

# MySQL 데이터베이스에 접속하기
mydb = mysql.connector.connect(
  host="localhost",
  user="systemuser",
  password="korea4302@#$",
  database="mydatabase"
)

print(mydb)
