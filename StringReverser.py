def reversal(stringy):
    arrry = []
    arrry_stingy = list(stringy)
    for x in range(len(stringy)):
        arrry.append(arrry_stingy[-x-1])
    # thing_reversed = str(arrry)
    thing_reversed = ''.join(arrry) #(i used chatgpt for this one line - i know i was having a dumb momenyt)

    return thing_reversed

stringy = input("Enter your string here: ")
print("Here is your reversed string: ",  reversal(stringy))
