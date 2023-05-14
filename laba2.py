passord_1 = input()
password_aprove = input()
if passord_1 == password_aprove :
    print("Пароль принят")
else:
    print("Пароль не принят")
def year (a):
    if (a%4 == 0 and a%100 != 0) or a%400 == 0 :
        print("Год ",a," - високосный")
    else:
        print("Этот год не високосный")

def z1 ():
    colors = ["красный","синий","желтый"]
    while True :
        color1 = input()
        if color1 in colors:
            break
        print("Это не основной цвет, введите другое слово")
    while True :
        color2 = input()
        if color2 in colors:
            break
        print("Это не основной цвет, введите другое слово")
    colors = [color1,color2]
    if "красный" in colors and "синий" in colors:
        print("фиолетовый")
    if "красный" in colors and "желтый" in colors:
        print("оранжевый")
    if "желтый" in colors and "синий" in colors:
        print("зеленый")

def check_input(phrase):
    while True:
        try:
            choise = int(input(phrase))
            break
        except:
            print("Введите чило от 1 до 4!")

    return choise

while True:

    print("\nДобро пожаловать на проверку практического задания номер 2 от Анны Мочалиной!")
    print()
    print("[1] - задание 1")

    print("[0] - выход")
    print()

    choise = check_input("Введите номер задания: ")

    if choise == 1:

        z1()

    elif choise == 0:
        print("Выход...")
        exit()
