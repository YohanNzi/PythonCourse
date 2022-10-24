import random

turn = 0
guess = 101

difficulty = int(input("\nSelectionnez la difficulté : \n0 = Random \n1 = Facile : 0 à 10. \n2 = Moyen : 0 à 100. \n3 = Difficile : 0 à 1000.\n"))
while difficulty > 3 :
    difficulty = int(input("\nSelectionnez la difficulté : \n1. Facile : 0 à 10. \n2. Moyen : 0 à 100. \n3. Difficile : 0 à 1000.\n"))

if difficulty == 0:
    number_to_guess = random.randint(0, random.randint(0, 1000))    
elif difficulty == 1:
    number_to_guess = random.randint(0, 10)
elif difficulty == 2:
    number_to_guess = random.randint(0, 100)
else :
    number_to_guess = random.randint(0, 1000)

while guess is not number_to_guess:
    guess = int(input("Entrer un nombre : "))

    if guess > number_to_guess :
        turn += 1
        print(f'Le nombre est plus petit que {guess}')
    else :
        turn += 1
        print(f'Le nombre est plus grand que {guess}')
        
print(f'Bravo, vous avez reussi en {turn} essais')

