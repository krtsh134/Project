from db import *
import json
from project import *
from tkinter import messagebox


def add_meal_plans(age_min, age_max, bmi_min, bmi_max, description, time, products_needed):
#ввод и вывод данных в консоль заменить на приложение
    cnct = sqlite3.connect('health_control.db')
    cursor = cnct.cursor()

    # age_max = input("Введите возраст 'до': ")
    # bmi_min = input("Введите ИМТ 'от': ")
    # bmi_max = input("Введите ИМТ 'до': ")
    # description = input("Введите описание: ")
    # time = input("Введите время приёма: ")
    # products_input = input("Введите продукты через запятую: ")

    # products_list = [product.strip() for product in products_input.split(',')]
    # products_needed = json.dumps(products_list)
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



def get_meal_plan(age, bmi, available_foods):
    meal_plan = {'breakfast': None, 'lunch': None, 'dinner': None}

    cnct = sqlite3.connect('health_control.db')
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
        max_matches = -1

        for description, products_needed in grouped_meals[meal_time]:
            needed_products = [product.strip().lower() for product in products_needed.split(',')]
            matches = sum(1 for food in available_foods if food in needed_products)
            
            if matches > max_matches:
                max_matches = matches
                best_match = (description, products_needed)
        
        if best_match and max_matches > 0:
            meal_plan[meal_time] = best_match
        
        else:
            meal_plan[meal_time] = first_meals[meal_time]
    
    return meal_plan

# def recomend_meals():
#     try:
#         age = int(age_entry.get())
#         bmi = float(bmi_entry.get())
#         available_foods = input(available_foods_entry.get()).split(',')

#         meal_plan = get_meal_plan(age, bmi, [food.strip().lower() for food in available_foods])

#         result_text.delete(1.0, tk.END)
#         result_text.insert(tk.END, "Ваш план питания:/n")

#         for meal_time in ['breakfast', 'lunch', 'dinner']:
#             description, products_needed = meal_plan[meal_time]
#             result_text.insert(tk.END, f"{meal_time.capitalize()}: {description} (Продукты: {products_needed})\n")

#     except ValueError:

#         messagebox.showerror("Ошибка", "Пожалуйста, введите корректные значения для возраста и ИМТ")

# if __name__ == "__main__":
#     main()

#add_meal_plans()


    # age = input("Введите Ваш возраст: ").strip().lower()
    # bmi = input("Введите Ваш ИМТ: ").strip().lower()
    # user_products = input("Введите Ваши продукты: ").strip().lower()

    # try:
    #     sql = """
    #         SELECT meal_plan FROM MealPans 
    #         WHERE goal = ? AND user_products LIKE ?
    #     """
    #     cursor.execute(sql, (age, bmi, f'%{user_products}%'))
    #     meal_plans = cursor.fetchall()

    #     if meal_plans:
    #         print('\nВаш план питания: ')
    #         for plan in meal_plans:
    #             print(plan[0])
    #     else:
    #         print("Извините, не найдено подходящего плана питания.")
    # except sqlite3.Error as e:
    #     print(f"Ошибка при получении плана питания: {e}")
    # finally:
    #     cnct.close()



# def add_meal_plan(db, bmi_min, bmi_max, products, plan):
#     cnct = sqlite3.connect(db)
#     cursor = cnct.cursor()
#     try:
#         cursor.execute("""
#             INSERT INTO MealPlans (bmi_min, bmi_max, products, plan) 
#             VALUES (?, ?, ?, ?)
#         """, (bmi_min, bmi_max, json.dumps(products), json.dumps(plan)))
#         cnct.commit()
#         print("Meal plan added successfully!") #Поменять на вывод в прилку
#     except sqlite3.Error as e:
#         print(f"Error adding meal plan: {e}")
#         cnct.rollback()
#     finally:
#         cnct.close()

# def get_meal_plan(db, bmi, user_products):
#     cnct = sqlite3.connect(db)
#     cursor = cnct.cursor()
#     try:
#         cursor.execute("""
#             SELECT products, plan FROM Meal_Plans 
#             WHERE bmi_max <= ? AND bmi_max >= ? 
#             ORDER BY LENGHT(products) ASC -- Prioritize plans with fewer products 
#             LIMIT 1
#         """, (bmi, bmi)) #вместо знака вопроса данные пользователя (bmi)
#         result = cursor.fetchone()
#         if result:
#             products_json, plan_json = result
#             products_needed = json.loads(products_json)
#             plan  = json.loads(plan_json)
#             missing_products = set(products_needed) - set(user_products)
#             return {"plan": plan, "missing_products": list(missing_products)}
#         else:
#             return {"plan": None, "missing_products": []}
#     except sqlite3.Error as e:
#         print(f"Error fetching meal plan: {e}")
#         return {"plan": None, "missing_products": []}
#     finally:
#         cnct.close()