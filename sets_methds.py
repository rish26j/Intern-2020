random_numbers = {1,2,3,2,4,5,4,6,3,6,8,9,5,3,2,4,2}

random_numbers.add(7)

print(random_numbers)

random_numbers.remove(7)

print(random_numbers)

rand_num = random_numbers.copy()

print(rand_num)

rand_num.clear()

print(rand_num)

print(random_numbers | rand_num)

print(rand_num & rand_num)