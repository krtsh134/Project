from db import *
from project import *
from tkinter import messagebox


def add_train_plans(age_min, age_max, bmi_min, bmi_max, train_number, gendr, description_train):
    '''Добавляет новый тренировочный план в базу данных.

    Эта функция принимает параметры для создания нового плана тренировок и добавляет их в таблицу
    TrainPlans базы данных health_control.db. В случае успешного добавления данных выводится сообщение
    об успешном завершении операции, в противном случае отображается сообщение об ошибке.

    :param age_min: Минимальный возраст для плана тренировок.
    :type age_min: int
    :param age_max: Максимальный возраст для плана тренировок.
    :type age_max: int
    :param bmi_min: Минимальный индекс массы тела (BMI) для плана тренировок.
    :type bmi_min: float
    :param bmi_max: Максимальный индекс массы тела (BMI) для плана тренировок.
    :type bmi_max: float
    :param train_number: Номер тренировочного плана.
    :type train_number: int
    :param gendr: Пол, для которого предназначен план ('male' или 'female').
    :type gendr: str
    :param description_train: Описание тренировочного плана.
    :type description_train: str
    :raises sqlite3.Error: Если возникает ошибка при выполнении запроса к базе данных.
    :raises ValueError: Если переданы неверные типы данных.'''
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
    '''Получает планы тренировок на основе возраста, индекса массы тела (BMI) и пола.

    Эта функция выполняет запрос к базе данных для получения списка тренировочных планов,
    соответствующих заданным параметрам: возрасту, индексу массы тела и полу. 
    Результаты запроса возвращаются в виде списка кортежей, содержащих номера тренировок и их описания.

    :param age: Возраст пользователя.
    :type age: int

    :param bmi: Индекс массы тела пользователя.
    :type bmi: float

    :param gendr: Пол пользователя ('male' или 'female').
    :type gendr: str

    :global trains: Глобальная переменная для хранения полученных планов тренировок.
    :type trains: list

    :returns: Список кортежей, каждый из которых содержит номер тренировки и её описание.
    :rtype: list of tuples or None

    :raises sqlite3.Error: Если возникает ошибка при выполнении запроса к базе данных.'''
    global trains
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
