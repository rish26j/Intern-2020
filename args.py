def sum_of_all_nums(*args):
    total=0
    for num in args:
        total+=num
    return total

print(sum_of_all_nums(3,6,5,2,8,9,33,42))

def credentials(*args):
    if "Rishabh" in args or "Jain" in args:
        return("Welcome back Rishabh")
    return("I'm unable to identify you.")


print(credentials("Virat","Lionel","BECKHAM","Robert","Rishabh"))