nums = [1,2,3,4,5,6]
is_true = all(num%2==0 for num in nums)
print(is_true)

is_false = any(num%2==0 for num in nums)
print(is_false)

people = ["Rishabh","Rock","Ryan","Robert","Ronaldo","Roger"]
truth = all(char[0]=="R" for char in people)
print(truth)