a = "._ "
b = "_... "
c = "_._. "
d = "_.. "
e = ". "
f = ".._. "
g = "__. "
h = ".... "
i = ".. "
j = ".___ "
k = "_._ "
l = "._.. "
m = "__ "
n = "_. "
o = "___ "
p = ".__. "
q = "__._ "
r = "._. "
s = "... "
t = "_ "
u = ".._ "
v = "..._ "
w = ".__ "
x = "_.._ "
y = "_.__ "
z = "__.. "
space = "   "

phrase = input("Enter the sentence you wish to be translated: ").lower()
phrase_split = list(phrase)

#new skill!!
alphabets = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f,
    'g': g,
    'h': h,
    'i': i,
    'j': j,
    'k': k,
    'l': l,
    'm': m,
    'n': n,
    'o': o,
    'p': p,
    'q': q,
    'r': r,
    's': s,
    't': t,
    'u': u,
    'v': v,
    'w': w,
    'x': x,
    'y': y,
    'z': z,
    ' ': space
}
# print(a)
translated_phrase = []

# for x in range(1, len(phrase_split)):
for x in phrase_split:
    # print("success1")
    # print(x)
    if x in alphabets: #(just to make sure what they entered is a letter)
    #     print("success2")
    #     translated_phrase.append(x)
        translated_phrase.append(alphabets[x])

        # for y in alphabets:
        #     print("success3")
        #     if x == y:
        #         translated_phrase.append(y)
        #         print(y)
        #         break

translated_phrase = "".join(translated_phrase) #  new skill!

print(translated_phrase) # test!!!

    # basically i want to compare x (the current letter to one of the alphabets
    # whatever that letter is, the meaning is stored in a new list which will be converted into a string and outputted - without brackets


# currently it wont work because its comparing "a" == a (which is obviously false.