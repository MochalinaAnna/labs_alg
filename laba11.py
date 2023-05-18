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

def z_1():
    # Создаем экземпляр класса Restaurant и вызываем методы
    newRestaurant = Restaurant("Pizza Place", "Italian")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z_2():
    # Создаем три разных экземпляра класса Restaurant и вызываем метод describe_restaurant()
    restaurant1 = Restaurant("Burger Joint", "American")
    restaurant2 = Restaurant("Sushi Bar", "Japanese")
    restaurant3 = Restaurant("Taqueria", "Mexican")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z_3():
    # Обновляем рейтинг ресторана
    newRestaurant = Restaurant("Pizza Place", "Italian")
    newRestaurant.update_rating(4.5)
    newRestaurant.describe_restaurant()



while True:

    print("\nДобро пожаловать на проверку практического задания номер 11 от королевы вдохновения Анны Мочалиной!")
    print()
    print("[1] - Задача 11.1")
    print("[2] - Задача 11.2")
    print("[3] - Задача 11.3")
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