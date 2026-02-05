import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="",
    password="",
    port="5432",
    database="demo",
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
result = cursor.fetchall()

i = 0
name = input("Enter name: ")
for row in result:
    if row[0] == name:
        i += 1
        print(f"{i})", row)