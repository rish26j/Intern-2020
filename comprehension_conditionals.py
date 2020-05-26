cities = ["Jaipur","Hyderabad","Bombay","Delhi","Bangalore","Surat","Guwahati"]

cities2 = [city.upper() for city in cities]
print(cities2)

primes = [2,3,5,7,11,13,17,19]

primes2 = [x*x for x in primes]
print(primes2)

cities3 = [string for string in cities if string not in "Bombay" ]
print(cities3)