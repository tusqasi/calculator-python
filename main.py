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
    return x*y

def pow(x,exp):
    return x**exp

def lt(x,y):
    return x<y
def cadd(x,y):
    return [x[0]+y[0], x[1]+y[1]]
<<<<<<< HEAD
=======

def csub(x,y):
    return [x[0]-y[0], x[1]-y[1]]
>>>>>>> 20a989d (Add complex sub)
