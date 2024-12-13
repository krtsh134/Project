from db import *
from project import *
from tkinter import messagebox


def add_meal_plans(age_min, age_max, bmi_min, bmi_max, description, time, products_needed):

    cnct = sqlite3.connect('health_control.db')
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



def get_meal_plan(age, bmi, available_foods_list):
    meal_plan = {'breakfast': None, 'lunch': None, 'dinner': None}

    try:
        with sqlite3.connect('health_control.db') as cnct:
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
            print(available_foods_list)
            for meal_time in grouped_meals:
                best_match = None
                is_match = False

                for description, products_needed in grouped_meals[meal_time]:
                    needed_products = set(product.strip().lower() for product in products_needed.split(','))
                    matches = 0
                    for food in available_foods_list:
                        if food.lower().strip() in  ''.join(needed_products):
                            matches+=1
                            print( str(needed_products))
                    if matches > 0:
                        best_match = (description, products_needed)
                        is_match = True
            
                if is_match:
                    meal_plan[meal_time] = best_match
                else:
                    print(best_match)
                    meal_plan[meal_time] = first_meals[meal_time]

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")

    return meal_plan