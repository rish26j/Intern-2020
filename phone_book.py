contacts= []

isRunning = True

while isRunning:

    print("\n" * 50)
    print("================")
    print("1: Add Person")
    print("2: Delete Person")
    print("3: List People")
    print("4: Quit")
    print("================")
    print("\n")

    sel = input("Pick One: ")

    if sel == "1":

        person = []
        print("\n" * 20)

        name = input("Name: ")
        person.append(name)

        age = input("Age: ")
        person.append(age)

        address = input("Address: ")
        person.append(address)

        phoneNumber = input("Phone Number: ")
        person.append(phoneNumber)

        contacts.append(person)

    elif sel == "2":

        print("\n" * 20)

        count = 1
        for x in contacts:
            print(str(count) + ": " + x[0])
            count += 1

        deleted = int(input("Pick One: ")) - 1

        if deleted == len(contacts):

            del(contacts[deleted])

    elif sel == "3":

        print("\n" * 20)

        for x in contacts:

            print("Name: " + x[0])
            print("Age: " + x[1])
            print("Address: " + x[2])
            print("Phone Number: " + x[3])

            print("\n")

        input("Press enter/return to continue")

    elif sel == "4":
        isRunning = False