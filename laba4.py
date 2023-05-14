def z1():
    try:
        a = int(input("введите число, чтобы проверить деление на 3: "))
        b = a % 3
    except ValueError:
        print("введено не число!")
    else:
        if b == 0 and a != 0:
            print("число", a, "делится на 3!")
        elif a == 0:
            print("Введен ноль!")
        else:
            print("Число", a, "не делится на 3")

def z2():
    try:
        a = int(input("Введите число: "))
        b = 100/a
    except ZeroDivisionError:
        print("Введен 0!")
    except ValueError:
        print("Введено не число!")
    else:
        print("Результат деления 100 на введенное число: ", b)

def z3():
    date = str(input("Введите дату для проверки: "))
    if int(date[:2]) * int(date[3:5]) == int(date[-2:]):
        print("Дата", date, "реально магическая!")
    else:
        print(int(date[:2]))
        print(int(date[3:4]))
        print(int(date[-2:]))

        print("Какая то не магическая дата")

def z4():
    num = str(input("Введите номер билета для проверки: "))

    num1 = int(num[:len(num) // 2])
    num2 = int(num[-(len(num) // 2):])

    sum1 = 0
    sum2 = 0

    while num1 > 0:
        digit1 = num1 % 10
        sum1 += digit1

        digit2 = num2 % 10
        sum2 += digit2

        num1 = num1 // 10
        num2 = num2 // 10

    if sum1 == sum2:
        print("Билет", num, "счастливый!")
    else:
        print("Какой то несчастливый билет")

def check_input(phrase):
    while True:
        try:
            choise = int(input(phrase))
            break
        except:
            print("Введите чило от 1 до 4!")

    return choise

while True:

    print("\nДобро пожаловать на проверку практического задания номер 4 от Анны Мочалиной!")
    print()
    print("[1] - проверить делимость на 3")
    print("[2] - поделить 100 на число")
    print("[3] - проверить дату на магическую")
    print("[4] - проверить билет на счастливый")
    print("[0] - выход")
    print()

    choise = check_input("Введите номер задания: ")

    if choise == 1:

        z1()

    elif choise == 2:

        z2()

    elif choise == 3:

        z3()

    elif choise == 4:

        z4()

    elif choise == 0:
        print("Выход...")
        exit()
