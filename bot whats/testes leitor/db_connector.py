import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "senha",
    database = "fault_code"
)

print(mydb)

cursor = mydb.cursor()

search = "SELECT * FROM FAULTS_ACS"

cursor.execute(search)

result = cursor.fetchall()

for x in result:
    print(x)
