def prim_nums(numbs):
    if numbs > 1:
      for x in range(2, numbs):
        if numbs % x == 0:
          return "Not prime number"
          break
      return "Prime number"
    else:
        print("invalid number")


numbs = int(input("Enter number:"))
print(f"{numbs}: " , prim_nums(numbs))