import math
primos=[]

def prime(number):
    if not isinstance(number,int) or number<1:
        raise ValueError('there is no zeroth prime')

    if len(primos)<number:
        completarPrimos(number)
    return primos[number-1]

def completarPrimos(number):
    global primos
    cont=2
    if primos!=[]:
        cont=primos[-1]+1
    
    while len(primos)<number:
        if is_prime(cont):
            primos.append(cont)
        cont+=1

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for candidato in range(3,int(math.sqrt(number))+1,2):
        if number % candidato == 0:
            return False
    return True
    