number = 0
count = 0
marks = []

while True:
    try:
        number = input("Entrer un nombre positif : ")
        number = float(number)
    except ValueError:
        print("Ceci n'est pas un nombre ...")
    else:
        if number < 0:
            break
        else:
            marks.append(number)
            count += 1

try:
    result = sum(marks) / count
except ZeroDivisionError:
    print(f"Il y a : {count} note(s)")
else:
    if count == 0:
        print("Vous n'avez pas saisi de note ...")
    else:
        print(f"La moyenne des {count} notes est : {result:.2f}")