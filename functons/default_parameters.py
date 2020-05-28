def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def fn(a,b,fn=add):
    return fn(a,b)

print(divide(10,5))

print(fn(10,5,divide))
