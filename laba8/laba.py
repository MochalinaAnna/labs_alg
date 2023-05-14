from PIL import Image

def z1():
    filename = "paint1.jpg"
    with Image.open(filename) as img:
        img.load()

    cropped_img = img.crop((100, 75, 300, 150))
    cropped_img.save("c_paint1.jpg")

    img.show()

def z2():
    from PIL import Image
    a = {1: "8marta.jpg", 2: "23feb.jpg", 3: "hb.jpg", 4: "hn.jpg"}
    print("1 - 8 март"
          "2 - 23 февраля"
          "3 - день рождения"
          "4 - новый год")
    b = int(input("введите число:"))
    filename = a[b]
    with Image.open(filename) as img:
        img.load()
        img.show()

def z3():
    from PIL import Image, ImageDraw, ImageFont
    name = input("Введите имя именинника:")
    filename = "hb.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial.ttf", 20)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 100,15),
        name + " , с праздником!",
        font=font,
        fill=("#000000")
    )
    img.show()
    img.save(name + "namehb.jpg")
while True:

    print("\nДобро пожаловать на проверку практического задания номер 8 от Анны Мочалиной!")
    print()
    print("[1] - Задача 1")
    print("[2] - Задача 2")
    print("[3] - Задача 3")
    print("[0] - Выход")
    print()

    choise = int(input("Введите номер задания: "))

    if choise == 1:

        z1()

    elif choise == 2:

        z2()

    elif choise == 3:

        z3()

    elif choise == 0:
        print("Выход...")
        exit()
