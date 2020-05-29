num = [1,2,3,4,5,6]

doubles = list(map(lambda x: x*x,num))
print(doubles)


players = ["Messi","Ronaldo","Xavi","Maradona","De Bruyne","Mane"]

caps = list(map(lambda names: names.upper(),players))
print(caps)