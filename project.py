import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from MealPlans import *
from Train_plans import *
from count_nutritional_value import *
from count_nutritional_value import add_newfoods
#import db




def open_hello_window():
    global hello_window

    hello_window = tk.Tk()
    hello_window.title('Health Controller')
    hello_window.geometry("700x150+400+200") # wise x hight + right + down
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)

    welcome_label = tk.Label(hello_window, text="Добро пожаловать в приложение по отслеживанию здоровья!", font=Title_Font)
    welcome_label.pack(pady=20)

    next_button = tk.Button(hello_window, text="Далее", command=open_parametrs_window, width=10, font=Button_Font)
    next_button.pack(pady=10)

def open_parametrs_window():
    global hello_window, parametrs_window, height_entry, weight_entry, age_entry, gender, is_parametrs_window_open, bmi

    hello_window.destroy()
    
    is_parametrs_window_open = True

    parametrs_window = tk.Tk()
    parametrs_window.title("Ваши параметры")
    parametrs_window.geometry("300x300+600+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        parametrs_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_2 = tk.Label(parametrs_window, text="Введите ваши данные", font=Title_Font)
    welcome_label_2.grid(row=0, column=1, columnspan=2, pady=10)

    height_label = tk.Label(parametrs_window, text="Рост (см):", font=Message_Font)
    height_label.grid(row=1,column=1, padx=20, pady=5, sticky="w")
    height_entry = tk.Entry(parametrs_window)
    height_entry.grid(row=1, column=2, padx=20, pady=5, sticky="e")

    weight_label = tk.Label(parametrs_window, text="Вес (кг):", font=Message_Font)
    weight_label.grid(row=2,column=1, padx=20, pady=5, sticky="w")
    weight_entry = tk.Entry(parametrs_window)
    weight_entry.grid(row=2, column=2, padx=20, pady=5, sticky="e")

    age_label = tk.Label(parametrs_window, text="Возраст:", font=Message_Font)
    age_label.grid(row=3,column=1, padx=20, pady=5, sticky="w")
    age_entry = tk.Entry(parametrs_window)
    age_entry.grid(row=3, column=2, padx=20, pady=5, sticky="e")

    gender_label = tk.Label(parametrs_window, text="Пол:", font=Message_Font)
    gender_label.grid(row=4,column=1, padx=20, pady=5, sticky="w")
    gender_var = tk.StringVar(parametrs_window)
    gender_var.set("Мужской")  # Значение по умолчан
    gender_options = ["Мужской", "Женский"]
    gender_menu = tk.OptionMenu(parametrs_window, gender_var, *gender_options)
    gender_menu.grid(row=4,column=2, padx=20, pady=5, sticky="w")

    def save_data():
        global height, weight, age, gender, bmi
        try:
            height = float(height_entry.get())
            weight = float(weight_entry.get())
            age = float(age_entry.get())
            gender = gender_var.get()
            bmi = round(weight/((height/100)**2), -1)
            print(f"Рост: {height} см, Вес: {weight} кг, Возраст: {age}, Пол: {gender}, ИМТ: {bmi}")
            open_main_menu()
        except ValueError:
            print("Ошибка: Введите числовые значения.")

    save_and_next_button = tk.Button(parametrs_window, text="Сохранить и продолжить", command=save_data, font=Button_Font)
    save_and_next_button.grid(row=5, column=1, columnspan=2, padx=30, pady=10, sticky="w")

    parametrs_window.mainloop()


def open_main_menu():
    global main_window, parametrs_window, is_main_window_open, is_parametrs_window_open

    if is_parametrs_window_open:
        parametrs_window.destroy()

    is_main_window_open = True
    
    main_window = tk.Tk()
    main_window.title("Главное меню")
    main_window.geometry("400x330+550+100")
    try: 
        logo = tk.PhotoImage(file='logo.png')
        main_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)

    welcome_label_3 = tk.Label(main_window, text="Что хотите посмотреть?", font=Title_Font)
    welcome_label_3.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="w")

    train_button = tk.Button(main_window, text="План тренировок", command=open_train_window, font=Button_Font)
    train_button.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="w")
    
    foodplan_button = tk.Button(main_window, text="План питания", command=open_foodplan_window, font=Button_Font)
    foodplan_button.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

    counter_kcal_button = tk.Button(main_window, text="Счетчик калорий", command=open_counter_kcal_window, font=Button_Font)
    counter_kcal_button.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

    add_data_button = tk.Button(main_window, text="Ввести новые данные в базу данных", command=open_add_data_window, font=Button_Font)
    add_data_button.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

# def close_main_window():
#     global is_main_window_open
#     main_window.destroy()
#     is_main_window_open = False

def display_train_plan():
    try:
        results = get_train_plans(age, bmi, gender)

        if results:
            result_text_1.delete("1.0", tk.END)
            result_text_2.delete("1.0", tk.END)

            if results['Train_1']:
                result_text_1.insert(tk.END, f"Train_1\n{results['Train_1']}")
            else:
                result_text_1.insert(tk.END, "План тренировки 1 не найден")
            if results['Train_2']:
                result_text_2.insert(tk.END, f"Train_2\n{results['Train_2']}")
            else:
                result_text_2.insert(tk.END, "План тренировки 2 не найден")
        else:
            result_text_1.insert(tk.END, "Ошибка при извлечении данных.")
            result_text_2.insert(tk.END, "")
    except ValueError:
        result_text_1.insert(tk.END, "Неверный формат ввода возраста или ИМТ")
    except Exception as e:
        result_text_1.insert(tk.END, f"Произошла ошибка: {e}")

def open_train_window():
    global main_window, train_window, result_text_1, result_text_2, age_entry, bmi
    main_window.withdraw()
    train_window = tk.Tk()
    train_window.title("План тренировки")
    train_window.geometry("600x750+450+100")
    try:
        logo = tk.PhotoImage(file='logo.png')
        train_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_4 = tk.Label(train_window, text="Ваша тренировка на сегодня", font=Title_Font)
    welcome_label_4.pack(pady=20)

    get_plan = tk.Button(train_window, text="Получить тренировку", command=display_train_plan, font=Button_Font)
    get_plan.pack(pady=20)

    result_text_1 = tk.Text(train_window, width=50, height=10, font=Message_Font)
    result_text_1.pack(pady=10)

    result_text_2 = tk.Text(train_window, width=50, height=10, font=Message_Font)
    result_text_2.pack(pady=10)

    main_menu_button = tk.Button(train_window, text="Вернуться в главное меню", command=return_to_main_menu, font=Button_Font) 
    main_menu_button.pack(pady=5)

def return_to_main_menu():
    train_window.destroy()
    main_window.deiconify()

def display_meal_plan():
    try:
        available_foods_input = available_foods_entry.get()

        available_foods_list = [food.strip().lower() for food in available_foods_input.split(',')]
        meal_plan = get_meal_plan(age, bmi, available_foods_list)

        meal_plan_str = "\n".join(f"{meal}: {desc} (Продукты: {prod})" for meal, (desc, prod) in meal_plan.items() if desc is not None)

        result_text.delete(1.0, tk.END)

        if meal_plan_str:
            result_text.insert(tk.END, meal_plan_str)
        else:
            result_text.insert(tk.END, "Нет подходящих планов питания")
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Ошибка ввода: Пожалуйста, введите корректные значения для возраста и ИМТ.")

def open_foodplan_window():
    global main_window, foodplan_window, available_foods_entry, result_text, age_entry, bmi, available_foods_entry, result_text
    main_window.withdraw()

    foodplan_window = tk.Tk()
    foodplan_window.title("План питания")
    foodplan_window.geometry("500x600+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        foodplan_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_5 = tk.Label(foodplan_window, text="Ваш план питания на сегодня", font=Title_Font)
    welcome_label_5.pack(pady=20)
    
    foodplan_window_label = tk.Label(foodplan_window, text="Введите Ваши продукты через запятую:")
    foodplan_window_label.pack(pady=5)
    available_foods_entry = tk.Entry(foodplan_window)
    available_foods_entry.pack(pady=5)

    get_recom = tk.Button(foodplan_window, text="Получить план питания", command=display_meal_plan)
    get_recom.pack(pady=20)

    result_text = tk.Text(foodplan_window, width=50, height=10)
    result_text.pack(pady=10)

    main_menu_button = tk.Button(foodplan_window, text="Главное меню", command=return_to_main_window, font=Button_Font)
    main_menu_button.pack(pady=5)

def return_to_main_window():
    foodplan_window.destroy()
    main_window.deiconify()

def open_counter_kcal_window():
    global main_window, counter_kcal_window, name_entry, size_entry, product_listbox, product_list, result_label
    main_window.withdraw()
    product_list=[]
    counter_kcal_window = tk.Tk()
    counter_kcal_window.title("Счетчик КБЖУ")
    counter_kcal_window.geometry("700x500+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        counter_kcal_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label = tk.Label(counter_kcal_window, text="Калькулятор энергетической ценности съеденных за день продуктов", font=Title_Font) # Changed from main_window
    welcome_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
    name_label = tk.Label(counter_kcal_window, text="Введите название продукта:", font=Message_Font) # Changed from main_window
    name_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
    name_entry = tk.Entry(counter_kcal_window)  # Changed from main_window
    name_entry.grid(row=1, column=1, padx=20, pady=5, sticky="e")
    size_label = tk.Label(counter_kcal_window, text="Введите массу продукта (в граммах):", font=Message_Font)  # Changed from main_window
    size_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
    size_entry = tk.Entry(counter_kcal_window)  # Changed from main_window
    size_entry.grid(row=2, column=1, padx=20, pady=5, sticky="e")
    add_button = tk.Button(counter_kcal_window, text="Добавить ещё продукт", command=add_product_for_counting, font=Button_Font) # Changed from main_window
    add_button.grid(row=3, column=0, padx=20, pady=10, sticky="e")
    calculate_button = tk.Button(counter_kcal_window, text="Посчитать мои КБЖУ за день", command=calculate_and_display, font=Button_Font)  # Changed from main_window
    calculate_button.grid(row=3, column=1, padx=20, pady=10, sticky="w")
    product_listbox = tk.Listbox(counter_kcal_window, width=50)  # Changed from main_window
    product_listbox.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
    product_listbox.config(height=5)
    result_label = tk.Label(counter_kcal_window, text="Ваши КБЖУ за день:", font=Message_Font, justify="left")  # Changed from main_window
    result_label.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="w")


def add_product_for_counting():
        """Adds a product to the list from the user interface, and displays it in the listbox."""
        global name_entry, size_entry, product_listbox, product_list
        name = name_entry.get().strip()
        weight_str = size_entry.get().strip()
        if not name or not weight_str:
          messagebox.showerror("Input Error", "Please enter both a product name and weight.")
          return
        try:
            weight = float(weight_str)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid weight.")
            return
        product_list.append((name, weight))
        product_listbox.insert(tk.END, f"{name}: {weight}g")
        # Clear input fields after adding
        name_entry.delete(0, tk.END)
        size_entry.delete(0, tk.END) 

def calculate_and_display():
    global result_label, product_list
    try:
        connection_db = sqlite3.connect("health_control.db")
        cursor_object = connection_db.cursor()
        cursor_object.execute(
                "SELECT name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms FROM Products"
            )
        table_Products_contents = {row[0].lower(): row[1:] for row in cursor_object.fetchall()}
        res_kcal = 0
        res_protein = 0
        res_fats = 0
        res_carbohydrates = 0
        for name, size in product_list:
                if name.lower() in table_Products_contents:
                    kcal, protein, fats, carbohydrates = table_Products_contents[name.lower()]
                    count_kcal = kcal * size / 100
                    count_protein = protein * size / 100
                    count_fats = fats * size / 100
                    count_carbohydrates = carbohydrates * size / 100
                    res_kcal += count_kcal
                    res_protein += count_protein
                    res_fats += count_fats
                    res_carbohydrates += count_carbohydrates
                else:
                    messagebox.showerror("Product Error", f"Product '{name}' not found.")
                    return  # Exit if product is not in the database
            #Update with calculated totals:
        result_text = (
                f"Килокалории: {round(res_kcal, 2)}\n"
                f"Белки: {round(res_protein, 2)}\n"
                f"Жиры: {round(res_fats, 2)}\n"
                f"Углеводы: {round(res_carbohydrates, 2)}"
            )
        result_label.config(text=result_text)
        product_list.clear()  #clear the list after the calculations.
        product_listbox.delete(0,tk.END) #Clear list box after calculations.
    except sqlite3.Error as e:
           messagebox.showerror("Database Error", f"Database error: {e}")
    except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
           if connection_db:
                connection_db.close()    



    
    # Лизина часть

def open_add_data_window():
    global main_window, add_data_window, is_add_data_window_open
    is_add_data_window_open = True
    # close_main_window()
    add_data_window = tk.Tk()
    add_data_window.title("Добавление данных")
    add_data_window.geometry("500x300+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        add_data_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_7 = tk.Label(add_data_window, text="Добавить новые данные", font=Title_Font)
    welcome_label_7.pack(pady=20)

    add_train_button = tk.Button(add_data_window, text="Добавить план тренировки", command=open_add_train_window, font=Button_Font) 
    add_train_button.pack(pady=5)

    add_foodplan_button = tk.Button(add_data_window, text="Добавить план питания", command=open_add_foodplan_window, font=Button_Font) 
    add_foodplan_button.pack(pady=5)
     #Ксюшина част

    add_newfood_button = tk.Button(add_data_window, text="Добавить КБЖУ нового продукта", command=open_add_newfood_window, font=Button_Font) 
    add_newfood_button.pack(pady=5) #Лизина часть

    main_menu_button = tk.Button(add_data_window, text="Главное меню", command=open_main_menu, font=Button_Font) 
    main_menu_button.pack(pady=5)

def open_add_train_window():
    global main_window, add_data_window, add_train_window
    add_data_window.destroy()
    add_train_window = tk.Tk()
    add_train_window.title("Добавление нового плана тренировок")
    add_train_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        add_train_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_8 = tk.Label(add_data_window, text="Добавьте новые данные о тренировке", font=Title_Font)
    welcome_label_8.grid(row=1,column=1, padx=20, pady=5, sticky="w")

    new_train_plan_label = tk.Label(add_train_window, text="Добавьте данные о тренировке:", font=Message_Font)
    new_train_plan_label.grid(row=2,column=1, padx=20, pady=5, sticky="w")
    new_train_plan_entry = tk.Entry(add_train_window)
    new_train_plan_entry.grid(row=2, column=2, padx=20, pady=5, sticky="e")

    def save_data():
        global new_train_plan
        try:
            new_train_plan = str(new_train_plan_entry.get())
            print(f"Новый план тренировок: {new_train_plan}")
            open_main_menu()
        except ValueError:
            print("Ошибка: Введите текст.")

    save_and_next_button = tk.Button(add_data_window, text="Сохранить и выйти", command=save_data, font=Button_Font)
    save_and_next_button.grid(row=3, column=1, columnspan=2, padx=30, pady=10, sticky="w")

    ex_window_button = tk.Button(add_data_window, text="Назад", command=open_add_data_window, font=Button_Font) 
    ex_window_button.grid(row=4, column=1, columnspan=2, padx=30, pady=10, sticky="w")

    main_menu_button = tk.Button(add_data_window, text="Главное меню", command=open_main_menu, font=Button_Font) 
    main_menu_button.grid(row=5, column=1, columnspan=2, padx=30, pady=10, sticky="w")



#добавить план питания в бд готова
def add_meal_plan(): 
    age_min = add_age_min_entry.get()
    age_max = add_age_max_entry.get()
    bmi_min = add_min_bmi_entry.get()
    bmi_max = add_max_bmi_entry.get()
    description = add_description_entry.get()
    time = add_time_entry.get()
    products_input = add_products_entry.get()

    products_list = [product.strip().lower() for product in products_input.split(',')]
    products_str = ','.join(products_list)
    add_meal_plans(age_min, age_max, bmi_min, bmi_max, description, time, products_str)

def open_add_foodplan_window():
    global main_window, add_data_window, add_foodplan_window, add_age_min_entry, add_age_max_entry, add_min_bmi_entry, add_max_bmi_entry, add_description_entry, add_time_entry, add_products_entry

    add_data_window.withdraw()
    add_foodplan_window = tk.Tk()
    add_foodplan_window.title("Добавление нового плана питания")
    add_foodplan_window.geometry("500x400+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        add_foodplan_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_9 = tk.Label(add_foodplan_window, text="Добавьте новый план питания", font=Title_Font)
    welcome_label_9.grid(row=1,column=1, padx=20, pady=5, sticky="w")

    add_min_age_label = tk.Label(add_foodplan_window, text='Введите возраст (от): ')
    add_min_age_label.grid(row=3, column=1, pady=5, sticky="w")
    add_age_min_entry = tk.Entry(add_foodplan_window)
    add_age_min_entry.grid(row=3, column=2, pady=5, sticky="e")

    add_max_age_label = tk.Label(add_foodplan_window, text='Введите возраст (до): ')
    add_max_age_label.grid(row=4, column=1, pady=5, sticky="w")
    add_age_max_entry = tk.Entry(add_foodplan_window)
    add_age_max_entry.grid(row=4, column=2, pady=5, sticky="e")

    add_min_bmi_label = tk.Label(add_foodplan_window, text='Введите ИМТ (от): ')
    add_min_bmi_label.grid(row=5, column=1, pady=5, sticky="w")
    add_min_bmi_entry = tk.Entry(add_foodplan_window)
    add_min_bmi_entry.grid(row=5, column=2, pady=5, sticky="e")

    add_max_bmi_label = tk.Label(add_foodplan_window, text='Введите ИМТ (до): ')
    add_max_bmi_label.grid(row=6, column=1, pady=5, sticky="w")
    add_max_bmi_entry = tk.Entry(add_foodplan_window)
    add_max_bmi_entry.grid(row=6, column=2, pady=5, sticky="e")

    add_description_label = tk.Label(add_foodplan_window, text='Введите описание: ')
    add_description_label.grid(row=7, column=1, pady=5, sticky="w")
    add_description_entry = tk.Entry(add_foodplan_window)
    add_description_entry.grid(row=7, column=2, pady=5, sticky="e")

    add_time_label = tk.Label(add_foodplan_window, text='Введите время приёма: ')
    add_time_label.grid(row=8, column=1, pady=5, sticky="w")
    add_time_entry = tk.Entry(add_foodplan_window)
    add_time_entry.grid(row=8, column=2, pady=5, sticky="e")

    add_products_label = tk.Label(add_foodplan_window, text='Введите продукты (через запятую): ')
    add_products_label.grid(row=9, column=1, pady=5, sticky="w")
    add_products_entry = tk.Entry(add_foodplan_window)
    add_products_entry.grid(row=9, column=2, pady=5, sticky="e")

    add_foodplan_button = tk.Button(add_foodplan_window, text="Добавить план питания", command=add_meal_plan)
    add_foodplan_button.grid(row=10, columnspan=3, pady=20)

    to_add_data_window_button = tk.Button(add_foodplan_window, text="Назад", command=return_to_add_data_window)
    to_add_data_window_button.grid(row=11, columnspan=3, pady=(5, 20))

def return_to_add_data_window():
    add_foodplan_window.destroy()
    add_data_window.deiconify()

    # Ксюшина часть

def add_newfood():
    name = add_name_entry.get()
    kilocalories= add_kilocalories_entry.get()
    protein_gramms= add_protein_gramms_entry.get()
    fat_gramms = add_fat_gramms_entry.get()
    carbohydrates_gramms=add_carbohydrates_gramms_entry.get()
    serving_size_gramms=int(100)
    add_newfoods(name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms)

def open_add_newfood_window():
    global main_window, add_data_window, add_newfood_window, is_add_newfood_window_open, add_name_entry, add_kilocalories_entry, add_protein_gramms_entry, add_fat_gramms_entry, add_carbohydrates_gramms_entry
    add_data_window.destroy()
    is_add_newfood_window_open = True
    add_newfood_window = tk.Tk()
    add_newfood_window.title("Добавление нового продукта и его энергетической ценности")
    add_newfood_window.geometry("1200x400+300+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        add_newfood_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_9 = tk.Label(add_newfood_window, text="Добавить новый продукт и его энергетическую ценность", font=Title_Font)
    welcome_label_9.grid(row=1,column=1, padx=20, pady=5, sticky="w")

    add_name_label = tk.Label(add_newfood_window, text='Введите название нового продукта с большой буквы:', font=Message_Font)
    add_name_label.grid(row=3, column=1, padx=20, pady=5, sticky="w")
    add_name_entry = tk.Entry(add_newfood_window)
    add_name_entry.grid(row=3, column=2, padx=20, pady=5, sticky="e")

    add_kilocalories_label = tk.Label(add_newfood_window, text='Введите количество килокалорий, содержащихся в 100 граммах введённого Вами продукта:', font=Message_Font)
    add_kilocalories_label.grid(row=4, column=1,padx=20, pady=5, sticky="w")
    add_kilocalories_entry = tk.Entry(add_newfood_window)
    add_kilocalories_entry.grid(row=4, column=2,padx=20, pady=5, sticky="e")

    add_protein_gramms_label = tk.Label(add_newfood_window, text='Введите количество белков (в граммах), содержащихся в 100 граммах продукта:', font=Message_Font)
    add_protein_gramms_label.grid(row=5, column=1, padx=20, pady=5, sticky="w")
    add_protein_gramms_entry = tk.Entry(add_newfood_window)
    add_protein_gramms_entry.grid(row=5, column=2, padx=20, pady=5, sticky="e")

    add_fat_gramms_label = tk.Label(add_newfood_window, text='Введите количество жиров (в граммах), содержащихся в 100 граммах продукта:', font=Message_Font)
    add_fat_gramms_label.grid(row=6, column=1,padx=20, pady=5, sticky="w")
    add_fat_gramms_entry = tk.Entry(add_newfood_window)
    add_fat_gramms_entry.grid(row=6, column=2, padx=20, pady=5, sticky="e")

    add_carbohydrates_gramms_label = tk.Label(add_newfood_window, text='Введите количество углеводов (в граммах), содержащихся в 100 граммах продукта:', font=Message_Font)
    add_carbohydrates_gramms_label.grid(row=7, column=1, padx=20, pady=5, sticky="w")
    add_carbohydrates_gramms_entry = tk.Entry(add_newfood_window)
    add_carbohydrates_gramms_entry.grid(row=7, column=2, padx=20, pady=5, sticky="e")

    add_newfood_button = tk.Button(add_newfood_window, text="Сохранить и продолжить", command=add_newfood, font=Button_Font)
    add_newfood_button.grid(row=10, columnspan=3,padx=20, pady=20)

    to_add_data_window_button = tk.Button(add_newfood_window, text="Назад", command=back_to_add_data_window1, font=Button_Font)
    to_add_data_window_button.grid(row=11, columnspan=3,padx=20, pady=(5, 20))

    
def back_to_add_data_window1():
    global add_newfood_window, is_add_newfood_window_open
    add_newfood_window.destroy()
    add_data_window.deiconify()
    

if __name__ == "__main__":
    height, weight, age, gender = 0, 0, 0, ""
    open_hello_window()
    hello_window.mainloop()