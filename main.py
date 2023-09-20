print("hello world")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    if y==0:
        print("error")
        return 0
    return x/y
def mul(x,y):
    prod = 1
    for i in range(y):
        prod+=x
    return prod