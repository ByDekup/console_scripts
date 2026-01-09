import random as ran, cursor as cur, os

# высота и ширина карты
height = 46
width = 156

# создание разных биомов
water = {"char": "~", "color": ((0, 1), (50, 100), (200, 255))}
mountains = {"char": "▲", "color": ((130, 135), (133, 135), (130, 135))}
snow = {"char": "*", "color": (255, 255, 255)}
beach = {"char": ".", "color": ((200, 255), (200, 255), (0, 50))}
grass = {"char": "_", "color": ((50, 60), (200, 255), (100, 150))}

# функция генерации
def generate(teritory):
    colors = teritory["color"]
    if not teritory == snow:
        r = ran.randint(colors[0][0], colors[0][1])
        g = ran.randint(colors[1][0], colors[1][1])
        b = ran.randint(colors[2][0], colors[2][1])
    else:
        r = colors[0]
        g = colors[1]
        b = colors[2]
    print(f"\033[38;2;{r};{g};{b}m{teritory["char"]}\033[0m", end="", flush=True)

# основная отрисовка
while True:
    with cur.HiddenCursor():
        for y in range(height):
            for x in range(width):
                val = ran.randint(0, 100)
                # определение территории
                if val < 20: ter = water
                elif 20 <= val < 30: ter = beach
                elif 30 <= val < 65: ter = grass
                elif 65 <= val < 80: ter = mountains
                elif val >= 80: ter = snow
                generate(ter)
            print("")
    input("\nНажмите Enter чтобы сгенерировать заново: ")
    os.system("cls")


