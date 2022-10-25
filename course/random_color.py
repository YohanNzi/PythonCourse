import random
from sty import fg

def random_color() -> tuple:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
        
    return red, green, blue

def generate_color(r: int, g: int, b: int):
    return fg(r, g, b)

red, green, blue = random_color
color = generate_color(red,green,blue)
print(color, "Hello World !")