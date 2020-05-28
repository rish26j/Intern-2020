def sum_nums(*args):
    print(args)
    total=0
    for num in args:
        total+=num
    return total

num = (2,5,8,5,1,6,8)
print(sum_nums(*num))