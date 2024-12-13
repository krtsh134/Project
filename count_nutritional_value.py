from db import *
from project import *
from tkinter import messagebox

def counter_nutritional_value():
    global user_product, table_Products_contents, count_kcal, name_of_product, count_carbohydrates, count_fats, count_protein, kcal, protein, fats, carbohydrates
    connection_db = sqlite3.connect("health_control.db")
    cursor_object = connection_db.cursor()
    cursor_object.execute("SELECT name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms FROM Products")
    table_Products_contents ={row[0]: row[1:] for row in cursor_object.fetchall()}
    user_product={}
    count_kcal=0
    count_protein=0
    count_fats=0
    count_carbohydrates=0
    res_kcal=0
    res_protein=0
    res_fats=0
    res_carbohydrates=0
    while True:
        name_of_product=input("Введите название продукта (Для выхода нажмите 'q'): ")
        if name_of_product.lower() =='q':
            break
        size_of_product=float(input("Введите массу продукта в граммах: "))
        if name_of_product.capitalize() in table_Products_contents:
            kcal, protein, fats, carbohydrates=table_Products_contents[name_of_product.capitalize()]
            count_kcal=kcal*size_of_product/100
            count_protein=protein*size_of_product/100
            count_fats=fats*size_of_product/100
            count_carbohydrates=carbohydrates*size_of_product/100
        else:
            print("Вводите только те продукты, которые есть в Вашем плане питания")
        res_kcal+=count_kcal
        res_protein+=count_protein
        res_fats+=count_fats
        res_carbohydrates+=count_carbohydrates
    print("Ваши килокалории за день: ", round(res_kcal, 2))
    print("Ваши белки за день: ", round(res_protein, 2))
    print("Ваши жиры за день: ", round(res_fats, 2))
    print("Ваши углеводы за день: ", round(res_carbohydrates, 2))
    return round(res_kcal, 2), round(res_protein, 2), round(res_fats, 2), round(res_carbohydrates, 2)
      
def add_newfoods(name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms):
    cnct = sqlite3.connect('health_control.db')
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
    

    counter_nutritional_value()
        

        
           







        







