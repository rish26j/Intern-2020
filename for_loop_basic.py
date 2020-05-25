num = int(input("How many times do I have to tell you : "))
for repeat in range(num):
    print("Clean your room!")
    if repeat >= 3:
        print("Do you even listen anymore?")
        break