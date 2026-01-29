import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="",
    password="",
    port="5432",
    database="shop"
)

if conn:
    print("Database Connected")

cursor = conn.cursor()
cursor.execute("INSERT INTO users(name, surname, product) VALUES ('Atum', 'Pos', 'Phone')")

cursor.execute("SELECT * FROM Users")
result = cursor.fetchall()

for rol in result:
    print(rol)

cursor.close()
conn.close()