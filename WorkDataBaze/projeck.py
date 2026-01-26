import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="sasa",
    port="5432",
    database="Name"
)

print("DB")

cursor = conn.cursor()

cursor.execute("SELECT * FROM names")

result = cursor.fetchall()

for rol in result:
    for item in rol:
        print(item)

cursor.close()
conn.close()
