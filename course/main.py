

number = int(input("Quelle table voulez-vous afficher ? "))
table = []

for i in range(1, 11):
    if ((number*i) % 3 == 0):
        table.append(f'{number*i}*')
    else:
        table.append(number*i)
    
#     table.append(number*i)
# for result in table :
#     if result % 3 == 0:
#         index = table.index(result)
#         result = str(f'{result}*')
#         table[index] = result
    
print(table) #commentaire monoligne

# for i in range(1, 11):
#     table.append(number*i)


# numbers =  [8, 7, 11, 7, 2, 10, 5, 8]
# new_list = []

# for number in numbers :
#     if number not in new_list :
#         new_list.append(number)

# print(new_list)

"""
    Commentaire multiligne
"""
