word = input("Enter a word: ")
word_reved = input("Enter a word to be checked: ")

l1 = list((word).lower())
l2 = list((word_reved).lower())

if len(l1) != len(l2):
    print("Not anagrams - different length of words")

else:
    for x in range(len(l1)):
        if l1[x] == l2[-x-1]:
            continue
        else:
            print("Not an anagram!")
            quit()
    print("Its an anagram")


