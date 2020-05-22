test_str = "quarantine"

print("The original string is : " + test_str)

new_str = ""

for i in range(len(test_str)):
    if i != 3:
        new_str = new_str + test_str[i]

print("The new string is : " + new_str)