from db import *
from project import *
from tkinter import messagebox


def add_train_plans(age_min, age_max, bmi_min, bmi_max, train_number, gendr, description_train):
    try:
        with sqlite3.connect('health_control.db') as cnct:
            cursor = cnct.cursor()

        sql = """INSERT INTO TrainPlans 
        (age_min, age_max, bmi_min, bmi_max, train_number, gendr, description_train)
        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        
        cursor.execute(sql, (age_min, age_max, bmi_min, bmi_max, train_number, gendr, description_train))
        cnct.commit()
        messagebox.showinfo("Успех", "Данные добавлены")
    
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка", f"Не удалось добавить данные: {e}")
    except ValueError as e:
        messagebox.showerror("Ошибка", f"Неверный тип данных: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла непредвиденная ошибка: {e}")
        raise
    finally:
        print("Ввод данных завершен")


def get_train_plans(age, bmi, gendr):
    global trains
    """Получает тренировочные планы на основе возраста, ИМТ и пола."""
    trains_plan = []
    try:
        with sqlite3.connect('health_control.db') as cnct:
            cursor = cnct.cursor()
            print(f"Запрос: age={age}, bmi={bmi}, gendr={gendr}")  
            cursor.execute("""
                SELECT DISTINCT train_number, description_train FROM TrainPlans 
                WHERE age_min <= ? AND age_max >= ? AND bmi_min <= ? AND bmi_max >= ? AND gendr = ?
                ORDER BY train_number
            """, (age, age, bmi, bmi, gendr)) 
            trains = cursor.fetchall()
            print(list(set(trains)))
            for train_number, description_train in trains:
                trains_plan.append((train_number, description_train))
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        return None
    return trains_plan
