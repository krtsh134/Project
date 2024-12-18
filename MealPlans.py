from db import *
from project import *
from tkinter import messagebox


def add_meal_plans(age_min, age_max, bmi_min, bmi_max, description, time, products_needed, db_name='health_control.db'):
    '''
    """
    Добавляет планы питания в базу данных.

    Эта функция выполняет вставку данных о планах питания в таблицу MealPlans
    базы данных health_control.db. Данные включают минимальный и максимальный возраст,
    минимальный и максимальный индекс массы тела (BMI), описание плана, время
    и необходимые продукты.

    :param age_min: Минимальный возраст для плана питания.
    :type age_min: int
    :param age_max: Максимальный возраст для плана питания.
    :type age_max: int
    :param bmi_min: Минимальный индекс массы тела для плана питания.
    :type bmi_min: float
    :param bmi_max: Максимальный индекс массы тела для плана питания.
    :type bmi_max: float
    :param description: Описание плана питания.
    :type description: str
    :param time: Время, когда план питания должен быть выполнен.
    :type time: str
    :param products_needed: Список необходимых продуктов для плана питания.
    :type products_needed: str

    :raises Exception: Если возникает ошибка при работе с базой данных,
                       будет вызвано исключение с сообщением об ошибке.

    :return: None
        Функция не возвращает значения, но выводит сообщение об успехе или ошибке.
    '''
    cnct = sqlite3.connect(db_name)
    cursor = cnct.cursor()

    sql = """INSERT INTO MealPlans 
    (age_min, age_max, bmi_min, bmi_max, description, time, products_needed)
    VALUES (?, ?, ?, ?, ?, ?, ?)"""

    try:
        cursor.execute(sql, (age_min, age_max, bmi_min, bmi_max, description, time, products_needed))
        cnct.commit()
        messagebox.showinfo("Успех", "Данные добавлены")
    
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")

    cnct.close()
    print("Ввод данных завершен")



def get_meal_plan(age, bmi, available_foods_list, db_name='health_control.db'):
    """
    Получает план питания на основе возраста, индекса массы тела (BMI) и доступных продуктов.

    Эта функция извлекает планы питания из базы данных health_control.db на основе
    заданного возраста и BMI. Она также проверяет, какие продукты доступны, и выбирает
    наиболее подходящие варианты для завтрака, обеда и ужина.

    :param age: Возраст пользователя.
    :type age: int
    :param bmi: Индекс массы тела пользователя.
    :type bmi: float
    :param available_foods_list: Список доступных продуктов.
    :type available_foods_list: list of str

    :raises sqlite3.Error: Если возникает ошибка при работе с базой данных,
                           будет вызвано исключение с сообщением об ошибке.

    :return: Словарь с выбранными блюдами для завтрака, обеда и ужина.
             Структура возвращаемого значения:
             {
                 'breakfast': (description, products_needed) or None,
                 'lunch': (description, products_needed) or None,
                 'dinner': (description, products_needed) or None
             }
    """
    meal_plan = {'breakfast': None, 'lunch': None, 'dinner': None}

    try:
        with sqlite3.connect(db_name) as cnct:
            cursor = cnct.cursor()
            cursor.execute("""
            SELECT time, description, products_needed FROM MealPlans
            WHERE age_min <= ? AND age_max >= ? AND bmi_min <= ? AND bmi_max >= ?
            """, (age, age, bmi, bmi)) 

            meals = cursor.fetchall()

            first_meals = {'breakfast': None, 'lunch': None, 'dinner': None}
            grouped_meals = {}

            for meal_time, description, products_needed in meals:
                if meal_time not in grouped_meals:
                    grouped_meals[meal_time] = []
                grouped_meals[meal_time].append((description, products_needed)) 

                if first_meals[meal_time] is None:
                    first_meals[meal_time] = (description, products_needed)
            for meal_time in grouped_meals:
                best_match = None
                is_match = False

                for description, products_needed in grouped_meals[meal_time]:
                    needed_products = set(product.strip().lower() for product in products_needed.split(','))
                    matches = 0
                    for food in available_foods_list:
                        if food.lower().strip() in  ''.join(needed_products):
                            matches+=1
                    if matches > 0:
                        best_match = (description, products_needed)
                        is_match = True
            
                if is_match:
                    meal_plan[meal_time] = best_match
                else:
                    meal_plan[meal_time] = first_meals[meal_time]

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")

    return meal_plan