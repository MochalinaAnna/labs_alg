import random

def z_1():
    # создание словаря
    capitals = {
        'Russia': 'Moscow',
        'USA': 'Washington, D.C.',
        'France': 'Paris',
        'Germany': 'Berlin',
        'Japan': 'Tokyo'
    }

    # вывод всех пар ключ-значение
    for country, capital in capitals.items():
        print(country, capital)

    # вывод столицы для определенной страны
    country = 'Russia'
    if country in capitals:
        print(capitals[country])
    else:
        print('Страна не найдена')

    # сортировка и вывод словаря
    sorted_capitals = dict(sorted(capitals.items()))
    for country, capital in sorted_capitals.items():
        print(country, capital)

def z_2():
    # создание словаря с буквами и их ценностью
    letter_values = {
        'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
        'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2,
        'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
        'й': 4, 'ы': 4,
        'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
        'ш': 8, 'э': 8, 'ю': 8,
        'ф': 10, 'щ': 10, 'ъ': 10
    }

    # ввод слова пользователем
    word = input('Введите слово: ').lower()

    # вычисление стоимости слова
    score = sum(letter_values.get(letter, 0) for letter in word)

    # вывод стоимости слова
    print(f'Стоимость слова "{word}" равна {score} очкам.')

def z_3():
    # создание множества студентов и их языков
    students = {
        'John': {'English', 'French', 'German'},
        'Alice': {'Spanish', 'Italian', 'Russian'},
        'Bob': {'English', 'Chinese', 'Japanese'},
        'Kate': {'German', 'French', 'Italian'}
    }

    # создание множества всех языков
    all_languages = set()
    for languages in students.values():
        all_languages.update(languages)

    # вывод отсортированного списка языков
    sorted_languages = sorted(all_languages)
    print(sorted_languages)

    # вывод списка студентов, знающих каждый язык
    for language in sorted_languages:
        print(f'{language}:', end=' ')
        for name, languages in students.items():
            if language in languages:
                print(name, end=' ')
        print()


while True:

    print("\nДобро пожаловать на проверку практического задания номер 4 от королевы вдохновения Анны Мочалиной!")
    print()
    print("[1] - Задача 6.1")
    print("[2] - Задача 6.2")
    print("[3] - Задача 6.3*")
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