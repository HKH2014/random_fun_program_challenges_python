import random

string_list = input("Enter a list: ")
thing = string_list.split()
listA = []
for x in thing:
    x = int(x)
    listA.append(x)
# print(listA)

choices = ["asc" , "desc" , "none"]
selected = random.choice(choices)
# print(selected)

if selected == "asc":
    listA.sort()
    print("Your list by ascending order: " , listA)

elif selected == "desc":
    listA.sort(reverse=True)
    print("Your list by descending order: " , listA)

else:
    print("Your unsorted list: " , listA)




