class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        """Выводит информацию о ресторане."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Rating: {self.rating}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        print(f"The restaurant {self.restaurant_name} is now open!")

    def update_rating(self, new_rating):
        """Обновляет рейтинг ресторана."""
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация класса-наследника."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # Новый атрибут для списка сортов мороженого

    def display_flavors(self):
        """Выводит список сортов мороженого."""
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        """Добавляет сорт мороженого в список flavors."""
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        """Удаляет сорт мороженого из списка flavors."""
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Flavor '{flavor}' has been removed.")
        else:
            print(f"Flavor '{flavor}' is not in the list.")

    def check_flavor_availability(self, flavor):
        """Проверяет наличие сорта мороженого в списке flavors."""
        if flavor in self.flavors:
            print(f"Flavor '{flavor}' is available.")
        else:
            print(f"Flavor '{flavor}' is not available.")

def z_1():
    # Создаем экземпляр IceCreamStand и вызываем методы
    ice_cream_stand = IceCreamStand("Ice Cream Paradise", "Dessert")
    ice_cream_stand.describe_restaurant()

def z_2():
    ice_cream_stand = IceCreamStand("Ice Cream Paradise", "Dessert")
    ice_cream_stand.add_flavor("Vanilla")
    ice_cream_stand.add_flavor("Chocolate")
    ice_cream_stand.add_flavor("Strawberry")
    ice_cream_stand.display_flavors()
    ice_cream_stand.remove_flavor("Chocolate")
    ice_cream_stand.check_flavor_availability("Chocolate")

while True:

    print("\nДобро пожаловать на проверку практического задания номер 12 от королевы вдохновения Анны Мочалиной!")
    print()
    print("[1] - Задача 12.1")
    print("[2] - Задача 12.2")
    #print("[3] - Задача 12.3")
    print("[0] - выход")
    print()

    choise = int(input("Введите номер задания: "))

    if choise == 1:

        z_1()

    elif choise == 2:

        z_2()

    # elif choise == 3:

    #     z_3()


    elif choise == 0:
        print("Выход...")
        exit()