import tkinter as tk
import tkinter.font as tkFont
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
    global hello_window, parametrs_window, height, weight, age, gender

    hello_window.destroy()
    
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
        global height, weight, age, gender
        try:
            height = float(height_entry.get())
            weight = float(weight_entry.get())
            age = float(age_entry.get())
            gender = gender_var.get()
            print(f"Рост: {height} см, Вес: {weight} кг, Возраст: {age}, Пол: {gender}")
            open_main_menu()
        except ValueError:
            print("Ошибка: Введите числовые значения.")

    save_and_next_button = tk.Button(parametrs_window, text="Сохранить и продолжить", command=save_data, font=Button_Font)
    save_and_next_button.grid(row=5, column=1, columnspan=2, padx=30, pady=10, sticky="w")

    parametrs_window.mainloop()

def open_main_menu():
    global main_window, parametrs_window
    parametrs_window.destroy
    main_window = tk.Tk()
    main_window.title("Главное меню")
    main_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)

    welcome_label_3 = tk.Label(main_window, text="Что хотите посмотреть?", font=Title_Font)
    welcome_label_3.pack(pady=20)

    train_button = tk.Button(main_window, text="План тренировок", command=open_train_window, font=Button_Font)
    train_button.pack(pady=5)
    
    foodplan_button = tk.Button(main_window, text="План питания", command=open_foodplan_window, font=Button_Font)
    foodplan_button.pack(pady=5)

    counter_kcal_button = tk.Button(main_window, text="Счетчик калорий", command=open_counter_kcal_window, font=Button_Font)
    counter_kcal_button.pack(pady=5)

    add_data_button = tk.Button(main_window, text="Ввести новые данные в базу данных", command=open_add_data_window, font=Button_Font)
    add_data_button.pack(pady=5)

    edit_data_button = tk.Button(main_window, text="Изменить данные о себе", command=open_parametrs_window, font=Button_Font)
    edit_data_button.pack(pady=5)

def open_train_window():
    global main_window, train_window
    main_window.destroy
    train_window = tk.Tk()
    train_window.title("План тренировки")
    train_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_4 = tk.Label(train_window, text="Ваша тренировка на сегодня", font=Title_Font)
    welcome_label_4.pack(pady=20)

    # label с тренировкой из бд - после добавления моей бд добавлю lable, надо понять как подключить бд к функции

    # next_train_button = tk.Button(train_window, text="Следующая тренировка", command=, font=Button_Font) # сменяет тренировку, добавить команду
    # next_train_button.pack(pady=5) - нужно или нет?

    main_menu_button = tk.Button(train_window, text="Главное меню", command=open_main_menu, font=Button_Font) 
    main_menu_button.pack(pady=5)

def open_foodplan_window():
    global main_window, foodplan_window
    main_window.destroy
    foodplan_window = tk.Tk()
    foodplan_window.title("План питания")
    foodplan_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    # Ксюшина часть

def open_counter_kcal_window():
    global main_window, counter_kcal_window
    main_window.destroy
    counter_kcal_window = tk.Tk()
    counter_kcal_window.title("Счетчик каллорий")
    counter_kcal_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    # Лизина часть

def open_add_data_window():
    global main_window, add_data_window
    main_window.destroy
    add_data_window = tk.Tk()
    add_data_window.title("Добавление данных")
    add_data_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_7 = tk.Label(add_data_window, text="Добавить новые данные", font=Title_Font)
    welcome_label_7.pack(pady=20)

    add_train_button = tk.Button(add_data_window, text="Добавить план тренировки", command=open_add_train_window, font=Button_Font) 
    add_train_button.pack(pady=5)

    # add_foodplan_button = tk.Button(add_data_window, text="Добавить план питания", command=open_add_foodplan_window, font=Button_Font) 
    # add_foodplan_button.pack(pady=5) Ксюшина часть

    # add_newfood_button = tk.Button(add_data_window, text="Добавить КБЖУ нового продукта", command=open_add_newfood_window, font=Button_Font) 
    # add_newfood_button.pack(pady=5) Лизина часть

    main_menu_button = tk.Button(add_data_window, text="Главное меню", command=open_main_menu, font=Button_Font) 
    main_menu_button.pack(pady=5)

def open_add_train_window():
    global main_window, add_data_window, add_train_window
    add_data_window.destroy
    add_train_window = tk.Tk()
    add_train_window.title("Добавление нового плана тренировок")
    add_train_window.geometry("400x200+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        hello_window.iconphoto(False, logo)
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

#def open_add_foodplan_window():
    # Ксюшина часть
#def open_add_newfood_window():
    # Лизина часть

if __name__ == "__main__":
    height, weight, age, gender = 0, 0, 0, ""
    open_hello_window()
    hello_window.mainloop()