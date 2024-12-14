import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from MealPlans import *
from Train_plans import *
from count_nutritional_value import *
from count_nutritional_value import add_newfoods
import db




def open_hello_window():
    '''
    """
    Открывает приветственное окно приложения.

   Эта функция создает новое окно Tkinter (``hello_window``), которое отображает
   приветственное сообщение пользователю и кнопку для перехода к следующему шагу (вводу параметров).

   :global hello_window: Ссылка на приветственное окно (создается в этой функции).
   :type hello_window: tk.Tk

   :raises tk.TclError: Если файл logo.png не найден, выводится предупреждение в консоль.
   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
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
    '''
    """
    Открывает окно для ввода пользовательских параметров (рост, вес, возраст, пол).

   Эта функция создает новое окно Tkinter (``parametrs_window``), предназначенное для сбора
   информации о пользователе (рост, вес, возраст и пол). После ввода данных вычисляется
   индекс массы тела (ИМТ) и сохраняется в глобальные переменные. Затем происходит переход в главное меню.

   :global hello_window: Ссылка на приветственное окно (которое будет закрыто).
    :type hello_window: tk.Tk
   :global parametrs_window: Ссылка на окно параметров (создается в этой функции).
   :type parametrs_window: tk.Tk
   :global height_entry: Виджет `tk.Entry` для ввода роста пользователя (в см).
   :type height_entry: tk.Entry
   :global weight_entry: Виджет `tk.Entry` для ввода веса пользователя (в кг).
   :type weight_entry: tk.Entry
   :global age_entry: Виджет `tk.Entry` для ввода возраста пользователя.
   :type age_entry: tk.Entry
    :global gender: Переменная для хранения пола пользователя.
    :type gender: str
   :global is_parametrs_window_open: Флаг, указывающий, открыто ли окно параметров.
    :type is_parametrs_window_open: bool
   :global bmi: Переменная для хранения ИМТ пользователя.
    :type bmi: float

   :raises ValueError: Если пользователь вводит нечисловые значения в поля ввода (рост, вес, возраст), выводится сообщение об ошибке в консоль.
   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global hello_window, parametrs_window, height_entry, weight_entry, age_entry, gender, is_parametrs_window_open, bmi
    hello_window.destroy()
    
    is_parametrs_window_open = True

    parametrs_window = tk.Tk()
    parametrs_window.title("Ваши параметры")
    parametrs_window.geometry("300x300+600+200")

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
    gender_var.set("Мужской")  
    gender_options = ["Мужской", "Женский"]
    gender_menu = tk.OptionMenu(parametrs_window, gender_var, *gender_options)
    gender_menu.grid(row=4,column=2, padx=20, pady=5, sticky="w")

    def save_data():
        '''
        """
        Сохраняет введенные пользователем параметры (рост, вес, возраст, пол) и вычисляет ИМТ.

   Эта функция считывает значения роста, веса и возраста из соответствующих виджетов ввода,
   а также выбранный пол из выпадающего списка. Затем вычисляет индекс массы тела (ИМТ)
   и сохраняет все эти данные в глобальные переменные. После этого вызывает функцию `from_par_to_main()`
   для перехода в главное меню.

   :global height: Глобальная переменная для хранения роста пользователя (в см).
   :type height: float
   :global weight: Глобальная переменная для хранения веса пользователя (в кг).
   :type weight: float
   :global age: Глобальная переменная для хранения возраста пользователя.
   :type age: float
    :global gendr: Глобальная переменная для хранения пола пользователя.
    :type gendr: str
   :global bmi: Глобальная переменная для хранения индекса массы тела пользователя.
   :type bmi: float
   :global height_entry: Виджет `tk.Entry`, из которого считывается рост пользователя.
   :type height_entry: tk.Entry
   :global weight_entry: Виджет `tk.Entry`, из которого считывается вес пользователя.
   :type weight_entry: tk.Entry
   :global age_entry: Виджет `tk.Entry`, из которого считывается возраст пользователя.
   :type age_entry: tk.Entry
   :global gender_var: Переменная `tk.StringVar`, хранящая выбранный пол пользователя из `tk.OptionMenu`.
   :type gender_var: tk.StringVar

   :raises ValueError: Если пользователь не ввел числовые значения в поля роста, веса или возраста, выводится сообщение об ошибке в консоль.
   :raises Exception: Если возникает ошибка при вызове `from_par_to_main`, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
        global height, weight, age, gendr, bmi
        try:
            height = float(height_entry.get())
            weight = float(weight_entry.get())
            age = float(age_entry.get())
            gendr = gender_var.get()
            bmi = round(weight/((height/100)**2), -1)
            print(f"Рост: {height} см, Вес: {weight} кг, Возраст: {age}, Пол: {gendr}, ИМТ: {bmi}")
            from_par_to_main()
        except ValueError:
            print("Ошибка: Введите числовые значения.")

    save_and_next_button = tk.Button(parametrs_window, text="Сохранить и продолжить", command=save_data, font=Button_Font)
    save_and_next_button.grid(row=5, column=1, columnspan=2, padx=30, pady=10, sticky="w")

    parametrs_window.mainloop()

def from_par_to_main():
    '''
    """
    Закрывает окно с параметрами и возвращает пользователя в главное меню.

   Эта функция уничтожает окно с параметрами (``parametrs_window``) и открывает главное меню,
   вызывая функцию `open_main_menu`.

   :global parametrs_window: Ссылка на окно с параметрами, которое будет закрыто.
   :type parametrs_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или открытии главного меню, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    parametrs_window.destroy()
    open_main_menu()

def open_main_menu():
    '''
    """
    Открывает главное меню приложения, предоставляющее пользователю выбор действий.

   Эта функция создает новое окно Tkinter (``main_window``) с главным меню, которое позволяет
   пользователю перейти к различным разделам приложения:
     - План тренировок
     - План питания
     - Счетчик калорий
     - Ввод новых данных в базу данных

   :global main_window: Ссылка на главное окно приложения (создается в этой функции).
   :type main_window: tk.Tk
   :global parametrs_window: Ссылка на окно параметров (не используется в коде, но может быть нужна в других частях приложения).
   :type parametrs_window: tk.Tk
   :global is_main_window_open: Флаг, указывающий, открыто ли главное окно.
   :type is_main_window_open: bool
    :global is_parametrs_window_open: Флаг, указывающий, открыто ли окно параметров (не используется в коде, но может быть нужна в других частях приложения).
   :type is_parametrs_window_open: bool

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global main_window, parametrs_window, is_main_window_open, is_parametrs_window_open

    is_main_window_open = True
    
    main_window = tk.Tk()
    main_window.title("Главное меню")
    main_window.geometry("400x330+550+100")

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

def display_train_plan():
    '''
    """
    Получает и отображает планы тренировок на основе введенных пользователем данных.

   Эта функция запрашивает планы тренировок у функции `get_train_plans` и отображает
   их в виджетах `result_text_1` (для первого этапа) и `result_text_2` (для второго этапа).
    Также обрабатывает возможные ошибки ввода и ошибки при получении данных.

   :global result_text_1: Виджет `tk.Text`, в котором отображается первый вариант плана тренировки.
   :type result_text_1: tk.Text
   :global result_text_2: Виджет `tk.Text`, в котором отображается второй вариант плана тренировки.
   :type result_text_2: tk.Text
   :global age: Переменная, содержащая возраст пользователя (определена в другом месте).
   :type age: int
   :global bmi: Переменная, содержащая индекс массы тела пользователя (определена в другом месте).
   :type bmi: float
    :global gendr: Переменная, содержащая пол пользователя (определена в другом месте).
    :type gendr: str

   :raises ValueError: Если возникает ошибка при преобразовании типов данных, сообщение об ошибке вставляется в `result_text_1`.
    :raises Exception: Если возникает любое другое исключение, сообщение об ошибке вставляется в `result_text_1`.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    try:
        results = get_train_plans(age, bmi, gendr)
        if results:
            result_text_1.delete("1.0", tk.END)
            result_text_2.delete("1.0", tk.END)

            if results['Train_1']:
                result_text_1.insert(tk.END, f"Первый вариант тренировки:\n{results['Train_1']}")
            else:
                result_text_1.insert(tk.END, "План тренировки 1 не найден")
            if results['Train_2']:
                result_text_2.insert(tk.END, f"Второй вариант тренировки:\n{results['Train_2']}")
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
    '''
    """
    Открывает окно с планом тренировок, позволяющее пользователю получить рекомендации.

   Эта функция создает новое окно Tkinter (``train_window``), предназначенное для отображения
   рекомендаций по плану тренировок. Пользователь может нажать кнопку для получения
    первого и второго этапа тренировки.

   :global main_window: Ссылка на главное окно приложения (которое будет скрыто).
   :type main_window: tk.Tk
   :global train_window: Ссылка на окно плана тренировок (создается в этой функции).
   :type train_window: tk.Tk
   :global result_text_1: Виджет `tk.Text` для отображения первого этапа тренировки.
   :type result_text_1: tk.Text
    :global result_text_2: Виджет `tk.Text` для отображения второго этапа тренировки.
   :type result_text_2: tk.Text

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global main_window, train_window, result_text_1, result_text_2, age_entry, bmi
    main_window.withdraw()
    train_window = tk.Tk()
    train_window.title("План тренировки")
    train_window.geometry("600x750+450+50")

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
    '''
    """
    Закрывает окно с планами тренировок и возвращает пользователя в главное меню.

   Эта функция уничтожает окно с планами тренировок (``train_window``) и отображает главное меню,
   делая его видимым с помощью метода `deiconify`.

   :global train_window: Ссылка на окно с планами тренировок, которое будет закрыто.
   :type train_window: tk.Tk
   :global main_window: Ссылка на главное окно приложения, которое будет отображено.
   :type main_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или отображении главного меню, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    train_window.destroy()
    main_window.deiconify()

def display_meal_plan():
    '''
    """
    Получает и отображает план питания на основе введенных пользователем данных.

   Эта функция считывает введенные пользователем продукты, запрашивает план питания у функции
   ``get_meal_plan``, и отображает полученный план в виджете `result_text`. Также обрабатывает возможные ошибки ввода.

   :global available_foods_entry: Виджет `tk.Entry`, содержащий список имеющихся продуктов, введенных пользователем (через запятую).
   :type available_foods_entry: tk.Entry
   :global result_text: Виджет `tk.Text`, в котором отображается сгенерированный план питания.
   :type result_text: tk.Text
   :global age: Переменная, содержащая возраст пользователя (определена в другом месте).
   :type age: int
    :global bmi: Переменная, содержащая индекс массы тела пользователя (определена в другом месте).
   :type bmi: float

   :raises ValueError: Если возникает ошибка при вводе (например, если не удалось преобразовать строку в число), текст с ошибкой выводится в виджете result_text.
   :raises Exception: Если возникают другие исключения при запросе плана питания, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
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
    '''
    """
    Открывает окно с планом питания, позволяющее пользователю получить рекомендации по питанию.

   Эта функция создает новое окно Tkinter (``foodplan_window``), предназначенное для
   отображения рекомендаций по плану питания. Пользователь может ввести имеющиеся у него продукты (через запятую),
   и на основе этих данных будет отображен план питания.

   :global main_window: Ссылка на главное окно приложения (которое будет скрыто).
   :type main_window: tk.Tk
   :global foodplan_window: Ссылка на окно плана питания (создается в этой функции).
   :type foodplan_window: tk.Tk
   :global available_foods_entry: Виджет `tk.Entry` для ввода списка продуктов, имеющихся у пользователя.
   :type available_foods_entry: tk.Entry
   :global result_text: Виджет `tk.Text` для отображения текста с рекомендациями по плану питания.
   :type result_text: tk.Text

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global main_window, foodplan_window, available_foods_entry, result_text, age_entry, bmi, available_foods_entry, result_text
    main_window.withdraw()

    foodplan_window = tk.Tk()
    foodplan_window.title("План питания")
    foodplan_window.geometry("500x450+450+200")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_5 = tk.Label(foodplan_window, text="Ваш план питания на сегодня", font=Title_Font)
    welcome_label_5.pack(pady=20)
    
    foodplan_window_label = tk.Label(foodplan_window, text="Введите Ваши продукты через запятую:", font=Message_Font)
    foodplan_window_label.pack(pady=5)
    available_foods_entry = tk.Entry(foodplan_window)
    available_foods_entry.pack(pady=5)

    get_recom = tk.Button(foodplan_window, text="Получить план питания", command=display_meal_plan, font=Message_Font)
    get_recom.pack(pady=20)

    result_text = tk.Text(foodplan_window, width=50, height=10)
    result_text.pack(pady=10)

    main_menu_button = tk.Button(foodplan_window, text="Главное меню", command=return_to_main_window, font=Button_Font)
    main_menu_button.pack(pady=5)

def return_to_main_window():
    '''
    """
    Закрывает окно с планами питания и возвращает пользователя в главное меню.

   Эта функция уничтожает окно с планами питания (``foodplan_window``) и отображает главное меню,
   делая его видимым с помощью метода `deiconify`.

   :global foodplan_window: Ссылка на окно с планами питания, которое будет закрыто.
   :type foodplan_window: tk.Tk
   :global main_window: Ссылка на главное окно приложения, которое будет отображено.
   :type main_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или отображении главного меню, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    foodplan_window.destroy()
    main_window.deiconify()

def open_counter_kcal_window():
    '''
    """
    Открывает окно счетчика КБЖУ, позволяющее пользователю добавлять продукты и рассчитывать их суммарную энергетическую ценность.

   Эта функция создает новое окно Tkinter (``counter_kcal_window``), предназначенное для подсчета
   суммарной энергетической ценности продуктов. Пользователь может вводить названия продуктов и их размеры (в граммах),
   добавлять их в список и затем рассчитывать суммарные КБЖУ (килокалории, белки, жиры и углеводы).

   :global main_window: Ссылка на главное окно приложения (которое будет скрыто).
   :type main_window: tk.Tk
   :global counter_kcal_window: Ссылка на окно счетчика КБЖУ (создается в этой функции).
   :type counter_kcal_window: tk.Tk
   :global name_entry: Виджет `tk.Entry` для ввода названия продукта.
   :type name_entry: tk.Entry
   :global size_entry: Виджет `tk.Entry` для ввода размера продукта (в граммах).
   :type size_entry: tk.Entry
   :global product_listbox: Виджет `tk.Listbox` для отображения списка добавленных продуктов.
   :type product_listbox: tk.Listbox
   :global product_list: Список для хранения добавленных продуктов (кортежей с названием и размером).
   :type product_list: list
   :global result_label: Виджет `tk.Label` для отображения результатов вычислений.
   :type result_label: tk.Label

   :raises tk.TclError: Если файл logo.png не найден, выводится предупреждение в консоль.
   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global main_window, counter_kcal_window, name_entry, size_entry, product_listbox, product_list, result_label
    main_window.withdraw()
    product_list=[]
    counter_kcal_window = tk.Tk()

    counter_kcal_window.title("Счетчик КБЖУ")
    counter_kcal_window.geometry("750x370+400+200")
    try:
        logo = tk.PhotoImage(file='logo.png')
        counter_kcal_window.iconphoto(False, logo)
    except tk.TclError:
        print("Warning: logo.png not found.")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label = tk.Label(counter_kcal_window, text="Калькулятор энергетической ценности съеденных за день продуктов", font=Title_Font)
    welcome_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
    name_label = tk.Label(counter_kcal_window, text="Введите название продукта:", font=Message_Font) 
    name_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
    name_entry = tk.Entry(counter_kcal_window)  
    name_entry.grid(row=1, column=1, padx=20, pady=5, sticky="e")
    size_label = tk.Label(counter_kcal_window, text="Введите массу продукта (в граммах):", font=Message_Font)  
    size_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
    size_entry = tk.Entry(counter_kcal_window)  
    size_entry.grid(row=2, column=1, padx=20, pady=5, sticky="e")
    add_button = tk.Button(counter_kcal_window, text="Добавить ещё продукт", command=add_product_for_counting, font=Button_Font) 
    add_button.grid(row=3, column=0, padx=20, pady=10, sticky="e")
    calculate_button = tk.Button(counter_kcal_window, text="Посчитать мои КБЖУ за день", command=calculate_and_display, font=Button_Font)  
    calculate_button.grid(row=3, column=1, padx=20, pady=10, sticky="w")
    result_label = tk.Label(counter_kcal_window, text="Ваши КБЖУ за день:", font=Message_Font, justify="left")  
    result_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="w")
    product_listbox = tk.Listbox(counter_kcal_window, width=50)  
    product_listbox.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="w")
    product_listbox.config(height=5)
    


def add_product_for_counting(): 
    
    global name_entry, size_entry, product_listbox, product_list
    name = name_entry.get().strip()
    weight_str = size_entry.get().strip()
    if not name or not weight_str:
        messagebox.showerror("Input Error", "Please enter both a product name and weight.")
    try:
        weight = float(weight_str)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid weight.")
    product_list.append((name, weight))
    product_listbox.insert(tk.END, f"{name}: {weight}g")
    name_entry.delete(0, tk.END)
    size_entry.delete(0, tk.END) 

def calculate_and_display():
    '''
    """
    Вычисляет и отображает суммарную пищевую ценность продуктов из списка.

   Эта функция извлекает данные о продуктах из базы данных, вычисляет суммарное
   количество килокалорий, белков, жиров и углеводов на основе списка продуктов
   и их размеров, и отображает результат в виджете `result_label`. 
    Также очищает список продуктов `product_list` и список в виджете `product_listbox` после вычисления.

   :global result_label: Виджет `tk.Label` для отображения результатов вычислений.
   :type result_label: tk.Label
   :global product_list: Список кортежей, содержащих имя продукта (str) и его размер (int).
   :type product_list: list
   :global product_listbox: Виджет `tk.Listbox`, отображающий список продуктов.
   :type product_listbox: tk.Listbox

   :raises sqlite3.Error: Если возникает ошибка при работе с базой данных, отображается окно сообщения с ошибкой.
   :raises Exception: Если возникает ошибка, не связанная с базой данных (например, KeyError), отображается окно сообщения с ошибкой.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
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

def open_add_data_window():
    '''
    """
    Открывает окно добавления данных, предоставляющее пользователю выбор действий.

   Эта функция создает новое окно Tkinter (``add_data_window``), которое позволяет
   пользователю выбрать одно из следующих действий:
     - Добавить новый план питания
     - Добавить данные о новом продукте (КБЖУ)
     - Добавить новый план тренировок
     - Вернуться в главное меню.

   :global add_data_window: Ссылка на окно добавления данных (создается в этой функции).
   :type add_data_window: tk.Tk
   :global is_main_window_open: Флаг, указывающий, открыто ли главное окно.
   :type is_main_window_open: bool
   :global main_window: Ссылка на главное окно приложения.
   :type main_window: tk.Tk

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global add_data_window, is_main_window_open, main_window
    if is_main_window_open:
        main_window.destroy()
    add_data_window = tk.Tk()
    add_data_window.title("Добавление данных")
    add_data_window.geometry("500x300+500+200")


    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)

    welcome_label_7 = tk.Label(add_data_window, text="Добавить новые данные", font=Title_Font)
    welcome_label_7.pack(pady=20)

    add_foodplan_button = tk.Button(add_data_window, text="Добавить план питания", command=open_add_foodplan_window, font=Button_Font) 
    add_foodplan_button.pack(pady=5)

    add_newfood_button = tk.Button(add_data_window, text="Добавить КБЖУ нового продукта", command=open_add_newfood_window, font=Button_Font) 
    add_newfood_button.pack(pady=5) 

    add_train_button = tk.Button(add_data_window, text="Добавить план тренировки", command=open_add_train_window, font=Button_Font) 
    add_train_button.pack(pady=5)

    main_menu_button = tk.Button(add_data_window, text="Главное меню", command=return_to_main_from_add, font=Button_Font) 
    main_menu_button.pack(pady=5)

def return_to_main_from_add():
    '''
    """
    Закрывает окно добавления данных и возвращает пользователя в главное меню.

   Эта функция уничтожает окно добавления данных (``add_data_window``) и открывает главное меню,
   вызывая функцию `open_main_menu`.

   :global add_data_window: Ссылка на окно добавления данных, которое будет закрыто.
   :type add_data_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или открытии главного меню, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    add_data_window.destroy()
    open_main_menu()

def open_add_train_window():
    '''
    """
    Открывает окно добавления нового плана тренировок.

   Эта функция создает новое окно Tkinter, предназначенное для ввода информации о новом плане тренировок.
   Пользователь может ввести описание нового плана тренировок в текстовое поле.
   Функция включает в себя кнопку сохранения данных и перехода в главное меню, а также кнопку возврата в окно добавления данных.

   :global main_window: Ссылка на главное окно приложения (не используется напрямую, но может быть нужна в других частях программы).
   :type main_window: tk.Tk
   :global add_data_window: Ссылка на окно добавления данных (не используется напрямую, но может быть нужна в других частях программы).
   :type add_data_window: tk.Tk
   :global add_train_window: Ссылка на окно добавления тренировки (создается в этой функции).
   :type add_train_window: tk.Tk

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''

    global main_window, add_data_window, add_train_window
    add_train_window = tk.Tk()
    add_train_window.title("Добавление нового плана тренировок")
    add_train_window.geometry("600x250+500+200")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_8 = tk.Label(add_train_window, text="Добавьте новые данные о тренировке", font=Title_Font)
    welcome_label_8.grid(row=0,column=1, padx=20, pady=5, sticky="w")

    new_train_plan_label = tk.Label(add_train_window, text="Добавьте данные о тренировке:", font=Message_Font)
    new_train_plan_label.grid(row=1,column=1, padx=20, pady=5, sticky="w")
    new_train_plan_entry = tk.Entry(add_train_window)
    new_train_plan_entry.grid(row=2, column=2, padx=20, pady=5, sticky="w")

    def save_data():
        '''
        """
        Сохраняет введенный пользователем новый план тренировок и переходит в главное меню.

   Эта функция считывает данные, введенные пользователем в поле ввода нового плана тренировок
   (``new_train_plan_entry``), сохраняет их в глобальную переменную ``new_train_plan`` и
   переходит к главному меню (вызывая функцию `open_main_menu`).

   :global new_train_plan: Глобальная переменная для сохранения введенного плана тренировок.
   :type new_train_plan: str
   :global new_train_plan_entry: Виджет `tk.Entry`, содержащий новый план тренировок.
   :type new_train_plan_entry: tk.Entry

   :raises ValueError: Если пользователь не ввел текст (выводит сообщение об ошибке в консоль).
   :raises Exception: Если возникает ошибка при вызове `open_main_menu`.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
        global new_train_plan
        try:
            new_train_plan = str(new_train_plan_entry.get())
            print(f"Новый план тренировок: {new_train_plan}")
            open_main_menu()
        except ValueError:
            print("Ошибка: Введите текст.")

    save_and_next_button = tk.Button(add_train_window, text="Сохранить и выйти", command=save_data, font=Button_Font)
    save_and_next_button.grid(row=3, column=1, columnspan=2, padx=30, pady=10, sticky="w")

    ex_window_button = tk.Button(add_train_window, text="Назад", command=return_to_add_data_window_from_aT, font=Button_Font) 
    ex_window_button.grid(row=4, column=1, columnspan=2, padx=30, pady=10, sticky="w")

def add_meal_plan(): 
    '''
    """
    Собирает данные о новом плане питания из полей ввода и передает их в функцию ``add_meal_plans``.

   Эта функция считывает данные, введенные пользователем в полях ввода окна добавления нового плана питания,
   и передает их в функцию ``add_meal_plans`` для дальнейшей обработки (например, сохранения в базе данных).
    Также обрабатывает список продуктов, переводя их в нижний регистр и объединяя в строку, разделенную запятыми.

   :global add_age_min_entry: Виджет `tk.Entry`, содержащий минимальный возраст.
   :type add_age_min_entry: tk.Entry
   :global add_age_max_entry: Виджет `tk.Entry`, содержащий максимальный возраст.
   :type add_age_max_entry: tk.Entry
   :global add_min_bmi_entry: Виджет `tk.Entry`, содержащий минимальный ИМТ.
   :type add_min_bmi_entry: tk.Entry
   :global add_max_bmi_entry: Виджет `tk.Entry`, содержащий максимальный ИМТ.
   :type add_max_bmi_entry: tk.Entry
   :global add_description_entry: Виджет `tk.Entry`, содержащий описание плана питания.
   :type add_description_entry: tk.Entry
   :global add_time_entry: Виджет `tk.Entry`, содержащий время приема пищи.
   :type add_time_entry: tk.Entry
    :global add_products_entry: Виджет `tk.Entry`, содержащий необходимые продукты.
   :type add_products_entry: tk.Entry

   :raises Exception: Если происходит ошибка при получении данных из полей ввода или при обработке списка продуктов, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
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
    '''
    """
    Открывает окно добавления нового плана питания.

   Эта функция создает новое окно Tkinter, предназначенное для ввода информации о новом плане питания.
   Пользователь может ввести минимальный и максимальный возраст, минимальный и максимальный ИМТ,
   описание плана, время приема пищи и необходимые продукты.

   :global main_window: Ссылка на главное окно приложения.
   :type main_window: tk.Tk
   :global add_data_window: Ссылка на окно добавления данных (которое будет скрыто).
   :type add_data_window: tk.Tk
   :global add_foodplan_window: Ссылка на окно добавления плана питания (создается в этой функции).
   :type add_foodplan_window: tk.Tk
   :global add_age_min_entry: Виджет `tk.Entry` для ввода минимального возраста.
   :type add_age_min_entry: tk.Entry
   :global add_age_max_entry: Виджет `tk.Entry` для ввода максимального возраста.
   :type add_age_max_entry: tk.Entry
   :global add_min_bmi_entry: Виджет `tk.Entry` для ввода минимального ИМТ.
   :type add_min_bmi_entry: tk.Entry
   :global add_max_bmi_entry: Виджет `tk.Entry` для ввода максимального ИМТ.
   :type add_max_bmi_entry: tk.Entry
   :global add_description_entry: Виджет `tk.Entry` для ввода описания плана питания.
   :type add_description_entry: tk.Entry
   :global add_time_entry: Виджет `tk.Entry` для ввода времени приема пищи.
   :type add_time_entry: tk.Entry
   :global add_products_entry: Виджет `tk.Entry` для ввода необходимых продуктов.
   :type add_products_entry: tk.Entry

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''

    global main_window, add_data_window, add_foodplan_window, add_age_min_entry, add_age_max_entry, add_min_bmi_entry, add_max_bmi_entry, add_description_entry, add_time_entry, add_products_entry

    add_data_window.withdraw()
    add_foodplan_window = tk.Tk()
    add_foodplan_window.title("Добавление нового плана питания")
    add_foodplan_window.geometry("500x500+500+200")

    Title_Font = tkFont.Font(family="Comic Sans MS", size=16)
    Button_Font = tkFont.Font(family="Comic Sans MS", size=13)
    Message_Font = tkFont.Font(family="Comic Sans MS", size=12)

    welcome_label_9 = tk.Label(add_foodplan_window, text="Добавьте новый план питания", font=Title_Font)
    welcome_label_9.grid(row=1,column=1, padx=20, pady=5, sticky="w")

    add_min_age_label = tk.Label(add_foodplan_window, text='Введите возраст (от): ', font=Message_Font)
    add_min_age_label.grid(row=3, column=1, pady=5, sticky="w")
    add_age_min_entry = tk.Entry(add_foodplan_window)
    add_age_min_entry.grid(row=3, column=2, pady=5, sticky="e")

    add_max_age_label = tk.Label(add_foodplan_window, text='Введите возраст (до): ', font=Message_Font)
    add_max_age_label.grid(row=4, column=1, pady=5, sticky="w")
    add_age_max_entry = tk.Entry(add_foodplan_window)
    add_age_max_entry.grid(row=4, column=2, pady=5, sticky="e")

    add_min_bmi_label = tk.Label(add_foodplan_window, text='Введите ИМТ (от): ', font=Message_Font)
    add_min_bmi_label.grid(row=5, column=1, pady=5, sticky="w")
    add_min_bmi_entry = tk.Entry(add_foodplan_window)
    add_min_bmi_entry.grid(row=5, column=2, pady=5, sticky="e")

    add_max_bmi_label = tk.Label(add_foodplan_window, text='Введите ИМТ (до): ', font=Message_Font)
    add_max_bmi_label.grid(row=6, column=1, pady=5, sticky="w")
    add_max_bmi_entry = tk.Entry(add_foodplan_window)
    add_max_bmi_entry.grid(row=6, column=2, pady=5, sticky="e")

    add_description_label = tk.Label(add_foodplan_window, text='Введите описание: ', font=Message_Font)
    add_description_label.grid(row=7, column=1, pady=5, sticky="w")
    add_description_entry = tk.Entry(add_foodplan_window)
    add_description_entry.grid(row=7, column=2, pady=5, sticky="e")

    add_time_label = tk.Label(add_foodplan_window, text='Введите время приёма: ', font=Message_Font)
    add_time_label.grid(row=8, column=1, pady=5, sticky="w")
    add_time_entry = tk.Entry(add_foodplan_window)
    add_time_entry.grid(row=8, column=2, pady=5, sticky="e")

    add_products_label = tk.Label(add_foodplan_window, text='Введите продукты (через запятую): ', font=Message_Font)
    add_products_label.grid(row=9, column=1, pady=5, sticky="w")
    add_products_entry = tk.Entry(add_foodplan_window)
    add_products_entry.grid(row=9, column=2, pady=5, sticky="e")

    add_foodplan_button = tk.Button(add_foodplan_window, text="Добавить план питания", command=add_meal_plan, font=Button_Font)
    add_foodplan_button.grid(row=10, columnspan=3, pady=20)

    to_add_data_window_button = tk.Button(add_foodplan_window, text="Назад", command=return_to_add_data_window, font=Button_Font)
    to_add_data_window_button.grid(row=11, columnspan=3, pady=(5, 20))

def return_to_add_data_window_from_aT():
    '''
    """
    Возвращает пользователя в окно добавления данных из окна добавления тренировки.

   Эта функция уничтожает окно добавления тренировки (``add_train_window``)
   и отображает окно добавления данных (``add_data_window``), делая его видимым.

   :global add_train_window: Ссылка на окно добавления тренировки, которое будет закрыто.
   :type add_train_window: tk.Tk
   :global add_data_window: Ссылка на окно добавления данных, которое будет открыто.
   :type add_data_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или отображении нового, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.

   :rtype: None'''
    add_train_window.destroy()
    add_data_window.deiconify()

def return_to_add_data_window():
    '''
    """
    Возвращает пользователя в окно добавления данных из окна добавления плана питания.

   Эта функция уничтожает окно добавления плана питания (``add_foodplan_window``)
   и отображает окно добавления данных (``add_data_window``), делая его видимым.

   :global add_foodplan_window: Ссылка на окно добавления плана питания, которое будет закрыто.
   :type add_foodplan_window: tk.Tk
   :global add_data_window: Ссылка на окно добавления данных, которое будет открыто.
   :type add_data_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или отображении нового, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.

   :rtype: None'''
    add_foodplan_window.destroy()
    add_data_window.deiconify()

def add_newfood():
    '''
    """
    Собирает данные о новом продукте из полей ввода и вызывает функцию для добавления в базу данных.

   Эта функция извлекает данные о новом продукте (название, калорийность, белки, жиры, углеводы)
   из соответствующих виджетов ввода и передает их вместе с фиксированным размером порции (100 г)
   в функцию `add_newfoods` для добавления в базу данных.

   :global add_name_entry: Виджет `tk.Entry`, из которого считывается название нового продукта.
   :type add_name_entry: tk.Entry
   :global add_kilocalories_entry: Виджет `tk.Entry`, из которого считывается калорийность продукта (на 100 г).
   :type add_kilocalories_entry: tk.Entry
   :global add_protein_gramms_entry: Виджет `tk.Entry`, из которого считывается количество белков (на 100 г).
   :type add_protein_gramms_entry: tk.Entry
   :global add_fat_gramms_entry: Виджет `tk.Entry`, из которого считывается количество жиров (на 100 г).
   :type add_fat_gramms_entry: tk.Entry
   :global add_carbohydrates_gramms_entry: Виджет `tk.Entry`, из которого считывается количество углеводов (на 100 г).
   :type add_carbohydrates_gramms_entry: tk.Entry

    :raises Exception: Если возникает ошибка при вызове `add_newfoods`, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    name = add_name_entry.get()
    kilocalories= add_kilocalories_entry.get()
    protein_gramms= add_protein_gramms_entry.get()
    fat_gramms = add_fat_gramms_entry.get()
    carbohydrates_gramms=add_carbohydrates_gramms_entry.get()
    serving_size_gramms=int(100)
    add_newfoods(name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms)

def open_add_newfood_window():
    '''
    """
    Открывает окно для добавления нового продукта и его пищевой ценности.

   Эта функция создает новое окно Tkinter (``add_newfood_window``), предназначенное для
   ввода данных о новом продукте (название, калорийность, белки, жиры, углеводы).
   После ввода данных они сохраняются в базу данных.

   :global main_window: Ссылка на главное окно приложения (не используется в коде, но может быть нужна в других частях приложения).
    :type main_window: tk.Tk
    :global add_data_window: Ссылка на окно добавления данных (которое будет закрыто).
   :type add_data_window: tk.Tk
   :global add_newfood_window: Ссылка на окно добавления нового продукта (создается в этой функции).
   :type add_newfood_window: tk.Tk
   :global is_add_newfood_window_open: Флаг, указывающий, открыто ли окно добавления нового продукта.
    :type is_add_newfood_window_open: bool
   :global add_name_entry: Виджет `tk.Entry` для ввода названия нового продукта.
   :type add_name_entry: tk.Entry
   :global add_kilocalories_entry: Виджет `tk.Entry` для ввода калорийности продукта (на 100 г).
   :type add_kilocalories_entry: tk.Entry
   :global add_protein_gramms_entry: Виджет `tk.Entry` для ввода количества белков (на 100 г).
   :type add_protein_gramms_entry: tk.Entry
   :global add_fat_gramms_entry: Виджет `tk.Entry` для ввода количества жиров (на 100 г).
   :type add_fat_gramms_entry: tk.Entry
   :global add_carbohydrates_gramms_entry: Виджет `tk.Entry` для ввода количества углеводов (на 100 г).
   :type add_carbohydrates_gramms_entry: tk.Entry

   :raises Exception: Если возникает ошибка при создании или отображении окна, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    global main_window, add_data_window, add_newfood_window, is_add_newfood_window_open, add_name_entry, add_kilocalories_entry, add_protein_gramms_entry, add_fat_gramms_entry, add_carbohydrates_gramms_entry
    add_data_window.destroy()
    is_add_newfood_window_open = True
    add_newfood_window = tk.Tk()
    add_newfood_window.title("Добавление нового продукта и его энергетической ценности")
    add_newfood_window.geometry("1000x400+300+200")

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
    '''
    """
    Закрывает окно добавления нового продукта и возвращает пользователя в окно добавления данных.

   Эта функция уничтожает окно добавления нового продукта (``add_newfood_window``) и открывает окно
   добавления данных, вызывая функцию `open_add_data_window`.

   :global add_newfood_window: Ссылка на окно добавления нового продукта, которое будет закрыто.
   :type add_newfood_window: tk.Tk

   :raises Exception: Если происходит ошибка при закрытии окна или открытии окна добавления данных, будет вызвано исключение.

   :return: None
       Функция не возвращает значения.
   :rtype: None'''
    add_newfood_window.destroy()
    open_add_data_window()

if __name__ == "__main__":
    height, weight, age, gender = 0, 0, 0, ""
    open_hello_window()
    hello_window.mainloop()