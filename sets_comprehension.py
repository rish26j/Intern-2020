sentence = input("Enter a string : ")

if len({char for char in sentence if char in "aeiou"})==5:
    print("Your string contains all 5 vowels")
else:
    print("Your string doesn't contain all the vowels")
