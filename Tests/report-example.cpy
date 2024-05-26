#int counter

def power(base, exponent):
#{
    global counter
    counter = 1

    if exponent == 1:
        return base
    elif exponent == 0:
        return 1
    else:
        return base * power(base ,exponent - 1)
#}

#def main
#int pwr

counter = 0

pwr = power(2,8)

print(pwr)
print(counter)
