phone_number = "0265987412"
#phone_number = print(str(input("Entrer un numero de telephone :\n>>> ")))
result = ""

digits_mapping = {
    "0" : "zero",
    "1" : "un",
    "2" : "deux",
    "3" : "trois",
    "4" : "quatre",
    "5" : "cing",
    "6" : "six",
    "7" : "sept",
    "8" : "huit",
    "9" : "neuf"
}

for digit in phone_number:
    result += digits_mapping.get(digit, "[Character not mapped]").title() + " "

print(result)
#mapping



#.lower()