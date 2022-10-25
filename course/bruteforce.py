import random
import time
from itertools import product


# I. Générateur de mot de passe
def generate_pwd(length:int) -> str:
    lowercases = "abcdefghijklmnopqrstuvwxyz"
    uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "()[]:;!"

    characters = f"{lowercases}{uppercases}{digits}{specials}"

    result = ""
    for i in range(0, length):
        result += random.choice(characters)

    return result


# II. Programme de bruteforce
def bruteforce(pwd:str) -> None:
    lowercases = "abcdefghijklmnopqrstuvwxyz"
    uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "()[]:;!"

    characters = f"{lowercases}{uppercases}{digits}{specials}"

    for i in range(len(pwd) + 1):
        # https://docs.python.org/3/library/itertools.html#itertools.product
        for attempt in product(characters, repeat = i):
            if ''.join(attempt) == pwd:
                return ''.join(attempt)

# Calcul du temps du bruteforce pour "[mpz"
# Module time
start = time.time()
print(bruteforce("[mpz"))
end = time.time()

print(f"Execution time: {end - start}s")


# III. Nombre de combinaisons possibles
"""
Somme des caractères possibles : 26 + 26 + 10 + 7 = 69
Pour un mot de passe de 6 caractères, le calcul est le suivant :
    - 69**6 (69 Exposant 6) soit 107 918 163 081 possibilités
--
"""