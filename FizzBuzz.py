import time as t

limit = int(input("Enter a number that will be the limit: "))

# for x in range(limit + 1):
for x in range(1, limit + 1):
    if (x % 3 == 0) and (x % 5 == 0):
        print("FizzBuzz")
        t.sleep(1)
    elif x % 3 == 0:
        print("Fizz")
        t.sleep(1)
    elif x % 5 == 0:
        print("Buzz")
        t.sleep(1)
    else:
        print(x)
        t.sleep(1)
