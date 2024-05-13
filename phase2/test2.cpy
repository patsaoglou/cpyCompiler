#int var

def function1(x,y):
#{
    #int m , i
    global var
    var = 3
    if var>y and var>y:
        m = var
    elif y>x and y>var:
        m = y
    else:
        m = x
    return m
#}


def function2(x):
#{
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 4 
    if x<0:
        return counterFunctionCalls
    else:
        return function2(x-2)
#}
    


def custom(x,y):
#{
    #int a, b , c

    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    
    a = 2
    
    if not y%(a+1)!=(y//x)*x:
    #{
        counterFunctionCalls = counterFunctionCalls + 1
    #}
    else:
        return 0
#}

        

def counter():
#{
    ## count until 10##
    #int count
    count=0
    while count <=10:
    #{
        count=count+1
        print(count)
    #}
   
#}

#def main

## inside main ##
            
#int i
        
i = int(input())
print(i)

i=1
while i <=5: 
#{
    print(counter())
    i = i - 1
#}


print(function1(5,10))
print(function2(2024))
print(custom(i,3))
print(counter())
