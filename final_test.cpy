def divides(x,y,z):
#{
    ## body of divides ##
    if z == (x//y):
        return 1
    else:
        return 0
#}

def fib(x):
#{
    if x<=0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
#}