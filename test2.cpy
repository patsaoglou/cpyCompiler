## test program ##

#int var
#int counterFunctionCalls

def function1(x,y):
#{
    #int m
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
    ##loop##
#{
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 4 
    if x<0:
        return 
    else:
        return function2(x-2)
#}
    


def custom(x,y):
    #{
        #int a
        a=2
        global counterFunctionCalls
        counterFunctionCalls = counterFunctionCalls + 1
        if y%(a+1)!=(y//x)*x: ##loop##
            return 1
        else:
            return 0
    #}

        

def counter():
#{
    ## count until 10##
    #int count
    count=0
    while count <=10: ##loop##
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
    i = i - 40000
#}


print(function1(5,10))
print(function2(2024))
print(custom(i,3))
print(counter())
