import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="",
    port="5432",
    database="Name"
)

if conn:
    print("DB work")

corsor = conn.cursor()
corsor.excute("SELECT * FROM names")
result = corsor.fetchall()
print(result)