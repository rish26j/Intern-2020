cities = ["Jaipur","Hyderabad","Bombay","Delhi"]
print("Initial list is " + str(cities))

cities.append("Bangalore")
print("Appended list is " + str(cities))

cities.clear()
print("Cleared list is " + str(cities))

cities.extend(["Jaipur","Hyderabad","Bombay","Delhi"])
print("Extended list is " + str(cities))

cities.insert(4,"Bangalore")
print("List after insertion is " + str(cities))

cities.remove("Bangalore")
print("List after removal is " + str(cities))

cities.pop(3)
print("Popped list is " + str(cities))