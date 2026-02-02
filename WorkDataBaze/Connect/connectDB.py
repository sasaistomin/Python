import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="",
    password="",
    port="5432",
    database="root"
)
if conn:
    print("Database Connected")


cursor = conn.cursor()
cursor.execute("SELECT * FROM root")
result = cursor.fetchone()

login = result[0]
password = result[1]
print(login, password)

cursor.execute("SELECT * FROM root")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
conn.close()