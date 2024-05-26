
#int counterFunctionCalls 
def counter():
#{
    ## count until 10##
    #int count
    count = 0
    while count <= 10:
    #{
        count = count + 1
    #}

    return count
#}

def divides(x,y,z):
#{
    ## body of divides ##
    if z == (x//y):
        return 1
    else:
        return 0
#}

def calculatecubespace(x,y,z):
#{
    ## body of calculate_cube_space ##
    return x * y * z
#}

def power(base, exponent):
#{
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1
    else:
        return base * power(base ,exponent - 1)
#}

def factorial(n):
#{
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#}

def min3(x, y, z):
#{
    #int m
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    if x<y and x<z:
        m = x
    elif y<x and y<z:
        m = y
    else:
        m = z
    return m
#}

#def main
## inside main ##         
#int cnt, div, ccs, fact, pwr, min

cnt = 0
counterFunctionCalls = 0
while cnt <=100: 
#{
    cnt = cnt + counter()
#}

## ret = 1 ##
div = divides(cnt, cnt, 1)

## ret = 990 ##
ccs = calculatecubespace(10, 33, 3)

## ret = 3628800 ##
fact = factorial(10)

## ret = 256 ##
pwr = power(2, 8)

## ret = -3628800 ##
min =  min3(-ccs, -fact, -pwr)

if counterFunctionCalls == 0 or counterFunctionCalls == 1:
    print(counterFunctionCalls) 

print(cnt)
print(div)
print(ccs)
print(fact)
print(pwr)
print(min)
print(counterFunctionCalls)

