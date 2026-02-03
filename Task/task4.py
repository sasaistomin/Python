import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    user = "",
    password = "",
    port = "5432",
    database = "task"
)
if conn:
    print("Connected")

cursor = conn.cursor()

print("1) Добавить пользувателя")
print("2) Просмотреть всех пользуватель")
print("3) Удалить польувателя")
do = input("Виберить что вы хотите сделать: ")

if do == "1":
    name = input("Введите имя: ")
    city = input("Введите город пользувателя: ")
    prodyck = input("Введите продукт: ")
    cost = input("Введите цену прдукта: ")
    cursor.execute(f"INSERT INTO orders(nameUser, producs, cost, cityUser) VALUES('{name}', '{prodyck}', {cost}, '{city}');")
    conn.commit()
    if conn.commit():
        print("Committed")

elif do == "2":
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    for res in result:
        for item in res:
            print(item)

elif do == "3":
    wName = input("Введите имя пользувателя котого хотите удать: ")
    cursor.execute(f"DELETE FROM Orders WHERE nameUser = '{wName}';")
    conn.commit()
    if conn.commit():
        print("Committed")