num = [1,2,3,4,5,6]

doubles = list(map(lambda x: x*x,num))
print(doubles)


players = ["Messi","Ronaldo","Xavi","Maradona","De Bruyne","Mane"]

caps = list(map(lambda names: names.upper(),players))
print(caps)

names = [
    {"first":"Roger","last":"Federer"},
    {"first": "Rafael", "last": "Nadal"},
    {"first": "Novak", "last": "Djokovic"}
]

last_name = list(map(lambda names:names["last"],names))
print(last_name)