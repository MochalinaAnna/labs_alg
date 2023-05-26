from tkinter import *

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название {self.restaurant_name}.")
        print(f"Тип {self.cuisine_type}.")

    def open_restaurant(self):
        print("Открыт")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='мороженное'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'клубника',
            'мята',
            'лимон',
            'шоколад',
            'черешня',
            'ваниль',
        ]

    def display_flavors(self, canvas):
        canvas.create_text(100, 100, text="В " + self.restaurant_name.title() +
                           " в наличии такие вкусы как :", fill='red')
        y = 120
        for flavor in self.flavors:
            canvas.create_text(100, y, text=flavor, fill='black')
            y += 20

ice_car = IceCreamStand('LALALA')


root = Tk() #вызов окна
root.title("Вкусы:") # название окна
canvas = Canvas(root) # Создаем в окне
canvas.pack() # вывод
canvas.create_text(100, 50, text='Список вкусов:', fill='black')
ice_car.display_flavors(canvas)
root.mainloop() # для вывода