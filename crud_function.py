'''черновик БД для бота модуля 14_4'''

import sqlite3

'''ф-ия созд. табл. Products и содержит поля'''
def initiate_db():
    connection = sqlite3.connect("prod_dtb.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INT PRIMARY KEY,
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

def add_bd(id, title, description, price):
    check_bd = cursor.execute("SELECT * FROM Users WHERE id=?", (id,))
    if check_bd.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Users VALUES('{id}','{title}','{description}',{price})
    ''')
    connection.commit()




