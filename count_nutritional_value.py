from db import *
from project import *
from tkinter import messagebox



def add_newfoods(name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms, dbname='health_control.db', run_counter=True):
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
