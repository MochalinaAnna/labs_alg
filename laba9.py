import os
from PIL import Image
import csv

def z_1():
    # Путь к папке с исходными изображениями
    input_folder = "/mnt/c/Users/Inssurg3nt/Documents/CTF/python_labs/img_input"

    # Путь к папке для итоговых изображений
    output_folder = "/mnt/c/Users/Inssurg3nt/Documents/CTF/python_labs/img_output"

    # Создаем папку для итоговых изображений, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам в папке input_folder
    for filename in os.listdir(input_folder):
        # Проверяем, что файл - изображение
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Считываем изображение
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Применяем к нему операцию (например, изменяем размер)
                new_img = img.resize((500, 500))
                # Сохраняем итоговое изображение в папку output_folder
                new_img.save(os.path.join(output_folder, filename))


def z_2():
    # Путь к папке с исходными изображениями
    input_folder = "/path/to/input/folder"

    # Путь к папке для итоговых изображений
    output_folder = "/path/to/output/folder"

    # Создаем папку для итоговых изображений, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам в папке input_folder
    for filename in os.listdir(input_folder):
        # Проверяем, что файл - изображение и имеет нужное расширение
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Считываем изображение
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Применяем к нему операцию (например, изменяем размер)
                new_img = img.resize((500, 500))
                # Сохраняем итоговое изображение в папку output_folder
                new_img.save(os.path.join(output_folder, filename))

def z_3():

    filename = "data.csv"

    # Создаем словарь для хранения данных
    data = {}

    # Считываем данные из CSV-файла и сохраняем их в словаре
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # пропускаем заголовок
        for row in reader:
            product = row[0]
            quantity = int(row[1])
            price = int(row[2])
            data[product] = {"quantity": quantity, "price": price}

    # Вычисляем итоговую сумму расходов
    total_cost = sum(data[product]["quantity"] * data[product]["price"] for product in data)

    # Выводим данные в требуемом формате
    print("Нужно купить:")
    for product in data:
        quantity = data[product]["quantity"]
        price = data[product]["price"]
        print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"Итоговая сумма: {total_cost} руб.")


while True:

    print("\nДобро пожаловать на проверку практического задания номер 9 от королевы вдохновения Анны Мочалиной!")
    print()
    print("[1] - Задача 9.1")
    print("[2] - Задача 9.2")
    print("[3] - Задача 9.3")
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