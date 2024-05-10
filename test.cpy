#int counterFunctionCalls

def quad(x):
#{
    #int y
    def sqr(x):
    #{
        global counterFunctionCalls
        counterFunctionCalls = counterFunctionCalls + 1
        return x*x
    #}
    
    global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
   
    return y
#}
        
#def main
#int i
counterFunctionCalls = 0
