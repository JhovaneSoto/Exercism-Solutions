import math
def primes(limit):
    marked=[]
    out=[]
    for num in range(2,limit+1):
        if num not in marked:
            if is_prime(num):
                marked+=multiplos(num,limit)
                out.append(num)
    return out

def is_prime(num):
    for candidato in range(2,int(math.sqrt(num))+1):
        if num%candidato==0:
            return False
    return True

def multiplos(num,limite):
    out=[]
    cont=1
    while num*cont<limite:
        out.append(num*cont)
        cont+=1

    return out