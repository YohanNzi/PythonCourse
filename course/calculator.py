from decimal import DivisionByZero


def addition(a: int, b: int) -> int:
    return a + b

def substraction(a: int, b: int) -> int:
    return a - b

def multiplication(a: int, b: int) -> int:
    return a * b

def division(a: int, b: int) -> int:
    try :
        result = (a / b)
    except DivisionByZero:
        print("La division par zero est impossible ...")
    else:
        return result

