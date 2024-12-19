from db import *
from tkinter import messagebox


def add_newfoods(name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms, dbname='health_control.db'):
    """Добавляет новую запись о продукте в базу данных SQLite.

    :param name: Название продукта.
    :type name: str
    :param kilocalories: Количество килокалорий на порцию.
    :type kilocalories: int or float
    :param protein_gramms: Количество белков в граммах на порцию.
    :type protein_gramms: int or float
    :param fat_gramms: Количество жиров в граммах на порцию.
    :type fat_gramms: int or float
    :param carbohydrates_gramms: Количество углеводов в граммах на порцию.
    :type carbohydrates_gramms: int or float
    :param serving_size_gramms: Размер порции в граммах.
    :type serving_size_gramms: int or float
    :param dbname: Имя файла базы данных SQLite. По умолчанию используется 'health_control.db'.
    :type dbname: str
    """
    cnct = sqlite3.connect(dbname)
    cursor = cnct.cursor()
    sql = """INSERT INTO Products 
    (name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms)
    VALUES (?, ?, ?, ?, ?, ?)"""
    try:
        cursor.execute(sql, (name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms))
        cnct.commit()
        messagebox.showinfo("Данные успешно добавлены.")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")

    cnct.close()
    print("Ввод данных завершен")





