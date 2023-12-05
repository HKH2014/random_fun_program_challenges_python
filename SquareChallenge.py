
numbers = []
numbers_squared = []

def byebye():
    print("Have a great day! :) ")
    quit()

while True:
    try:
        x = int(input("Please enter a number. Alternatively, press enter to quit the program: "))
        numbers.append(x)
        again = input("Would you like to enter another number y/n? ").lower()
        if again == "y":
            continue
        else:
            break
    except ValueError:
        byebye()

for y in numbers:
    z = y * y
    numbers_squared.append(z)

print("Here are your entered numbers: ", numbers)
print("Here is the square of each number: " , numbers_squared)


