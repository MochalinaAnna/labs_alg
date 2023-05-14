from PIL import Image, ImageFilter


def z_1():
    img = Image.open("start.jpg")
    img.show()
    width, height = img.size
    print("Размер изображения: {}x{}".format(width, height))
    print("Формат изображения:", img.format)
    print("Цветовая модель изображения:", img.mode)

def z_2():
    img = Image.open("start.jpg")
    img.show()

    width, height = img.size
    small_img = img.resize((width // 3, height // 3))
    horiz_mirror = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    vert_mirror = img.transpose(method=Image.FLIP_TOP_BOTTOM)

    small_img.save("small_image.jpg")
    horiz_mirror.save("horizontal_mirror.jpg")
    vert_mirror.save("vertical_mirror.jpg")

def z_3():
    filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.EMBOSS, ImageFilter.SHARPEN, ImageFilter.EDGE_ENHANCE]
    for i in range(1, 6):
        img = Image.open(f"{i}.jpg")
        for f in filters:
            filtered_img = img.filter(f)
            filtered_img.save(f"filtered_{i}_{f.__name__}.jpg")


def z_4():
    watermark = Image.open("watermark.png")
    for i in range(1, 6):
        img = Image.open(f"{i}.jpg")
        img.paste(watermark, (0, 0), watermark)
        img.save(f"watermarked_{i}.jpg")


while True:

    print("\nДобро пожаловать на проверку практического задания номер 7 от  Анны Мочалиной!")
    print()
    print("[1] - Задача 7.1")
    print("[2] - Задача 7.2")
    print("[3] - Задача 7.3")
    print("[4] - Задача 7.4")
    print("[0] - выход")
    print()

    choise = int(input("Введите номер задания: "))

    if choise == 1:

        z_1()

    elif choise == 2:

        z_2()

    elif choise == 3:

        z_3()

    elif choise == 4:

        z_4()

    elif choise == 0:
        print("Выход...")
        exit()