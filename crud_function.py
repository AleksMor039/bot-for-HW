'''черновик БД для бота модуля 14_4'''

import sqlite3

'''ф-ия созд. табл. Products и содержит поля'''


def initiate_db():
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INT NOT NULL
     );
    ''')
    connection.commit()
    connection.close()


'''ф-ия возвр. записи из таблицы Products'''


def get_all_products():
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products


'''ф-ия добавляет запись в таблицу Products'''


def add_bd(id, title, description, price):
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    # проверка сущ. запись с таким id
    cursor.execute("SELECT * FROM Products WHERE id=?", (id,))
    if cursor.fetchone() is None:  # если записи нет, добавляем её
        cursor.execute(
            "INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
            (id, title, description, price))
        connection.commit()
        print(f"Продукт с id={id} успешно добавлен.")
    else:
        print(f"Продукт с id={id} уже существует.")
    connection.close()





