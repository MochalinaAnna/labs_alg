import os
from PIL import Image
import csv

def z_1():

    input_folder = "F:\python_labs\img_input"


    output_folder = "F:\python_labs\img_output"


    for filename in os.listdir(input_folder):
        # Проверяем, что файл - изображение
        if filename.endswith(".jpg"):
            with Image.open(os.path.join(input_folder, filename)) as img:
                new_img = img.resize((500, 500))
                new_img.save(os.path.join(output_folder, filename))


def z_2():

    input_folder = "F:\python_labs\img_input"


    output_folder = "F:\python_labs\img_output"

    for filename in os.listdir(input_folder):

        if filename.endswith(".jpg")  or filename.endswith(".png"):
            with Image.open(os.path.join(input_folder, filename)) as img:
                new_img = img.resize((500, 500))

                new_img.save(os.path.join(output_folder, filename))

def z_3():

    filename = "data.csv"


    data = {}


    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product = row[0]
            quantity = int(row[1])
            price = int(row[2])
            data[product] = {"quantity": quantity, "price": price}


    total_cost = sum(data[product]["quantity"] * data[product]["price"] for product in data)


    print("Нужно купить:")
    for product in data:
        quantity = data[product]["quantity"]
        price = data[product]["price"]
        print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"Итоговая сумма: {total_cost} руб.")


while True:

    print("\nДобро пожаловать на проверку практического задания номер 9 от Анны Мочалиной!")
    print()
    print("[1] - Задача 1")
    print("[2] - Задача 2")
    print("[3] - Задача 3")
    print("[0] - выход")
    print()

    choise = int(input("Введите номер задания: "))

    if choise == 1:

        z_1()

    elif choise == 2:

        z_2()

    elif choise == 3:

        z_3()


    elif choise == 0:
        print("Выход...")
        exit()