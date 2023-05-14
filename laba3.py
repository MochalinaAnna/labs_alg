N = int(input())
words = ""
for i in range(N):
    word = str(input())
    words += word + " "

print(words)

def z1 ():
    word = str (input())
    words = ""
    while word != "stop":
        words += word + " "
        word = str(input())
    print(words)

def z2 ():
    while ( word := str(input())) != "stop" :
        if "ф" in word or "Ф" in word :
            print("Ого, это редкое слово")
        else:
            print("Эх, жаль но это не редкое слово")

def z3 ():
    from random import randint
    health = 3
    while True :
        a = randint(1,100)
        b = randint(1,100)
        print(f"{a} + {b} = ",end="")
        res = input()
        while not res.isdigit() and res != "stop":
            print("error",end="")
            res = input()
        if res == "stop":
            break
        if health == 0 :
            break
        if int(res) == a+b :
            print("Верно")
        else:
            print("Неверно")
            health -= 1

def check_input(phrase):
    while True:
        try:
            choise = int(input(phrase))
            break
        except:
            print("Введите чило от 1 до 4!")

    return choise

while True:

    print("\nДобро пожаловать на проверку практического задания номер 3 от Анны Мочалиной!")
    print()
    print("[1] - задание 1")
    print("[2] - задание 2")
    print("[3] - задание 3")
    print("[0] - выход")
    print()

    choise = check_input("Введите номер задания: ")

    if choise == 1:

        z1()

    elif choise == 2:

        z2()

    elif choise == 3:

        z3()

    elif choise == 0:
        print("Выход...")
        exit()
