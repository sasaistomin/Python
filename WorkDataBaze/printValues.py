import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user = "",
    password = "",
    port = "5432",
    database = "root"
)
if conn:
    print("Connected")


cursor = conn.cursor()

cursor.execute("SELECT * FROM root")
result = cursor.fetchall()
for rov in result:
    print(rov)

cursor.execute("SELECT * FROM root")
result = cursor.fetchall()
name = result[0][0]
password = result[0][1]
print(name)
print(password)

cursor.execute(f"INSERT INTO Root(login, password) VALUES('varay', 'root');")
conn.commit()
if conn.commit():
    print("commit add")

cursor.execute("SELECT * FROM root")
result = cursor.fetchall()
name = result[2][0]
password = result[1][1]
print(name)
print(password)