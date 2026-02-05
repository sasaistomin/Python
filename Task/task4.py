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
    name = input("\nВведите имя: ")
    city = input("Введите город пользувателя: ")
    prodyck = input("Введите продукт: ")
    cost = input("Введите цену прдукта: ")

    cursor.execute(f"INSERT INTO orders(nameUser, producs, cost, cityUser) VALUES('{name}', '{prodyck}', {cost}, '{city}');")
    conn.commit()

elif do == "2":
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()

    print("\n")
    for res in result:
        print(res)

elif do == "3":
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()

    calum = 0
    print("\n")
    while calum < len(result):
        name = result[calum][0]
        prody = result[calum][1]
        print(f"{name}- {prody}")
        calum += 1
    wName = input("Введите имя пользувателя котого хотите удать: ")

    cursor.execute(f"DELETE FROM orders WHERE nameUser = '{wName}';")
    conn.commit()