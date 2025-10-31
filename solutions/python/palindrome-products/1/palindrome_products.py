import math

palindromos=[]
def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor<min_factor:
        raise ValueError("min must be <= max")
    producto_min=min_factor*min_factor
    producto_max=max_factor*max_factor
    
    palidromos_generar(max_factor)
    candidatos=[item for item in palindromos if item>= producto_min and item<=producto_max][::-1]
    factores=[]
    for candidato in candidatos:
        factores=[]
        for num in range(min_factor,max_factor+1):
            if candidato%num==0:
                other=candidato//num
                if other in range(min_factor,max_factor) and sorted([num,other]) not in factores:
                    factores.append(sorted([num,other]))
        if factores!=[]:
            break
    if factores==[]:
        candidato=None
    return (candidato,factores)
            


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor<min_factor:
        raise ValueError("min must be <= max")
    producto_min=min_factor*min_factor
    producto_max=max_factor*max_factor
    
    palidromos_generar(max_factor)
    candidatos=[item for item in palindromos if item>= producto_min and item<=producto_max]
    factores=[]
    for candidato in candidatos:
        factores=[]
        for num in range(min_factor,max_factor+1):
            if candidato%num==0:
                other=candidato//num
                if other in range(min_factor,max_factor) and sorted([num,other]) not in factores:
                    factores.append(sorted([num,other]))
        if factores!=[]:
            break
    if factores==[]:
        candidato=None
    return (candidato,factores)

def palidromos_generar(limite):
    impar=True
    tam=1
    global palindromos
    if not palindromos:
        inicio=0
    else:
        temp=palindromos[-1]
        tam=math.ceil(len(str(temp))/2)
        inicio=int(str(temp)[:tam])
        if len(str(temp))%2==0:
            impar=False
        else:
            impar=True

    tam=None
    par=[]
    impar=[]
    for num in range(inicio+1,limite+1):
        cad=str(num)
        
        if not tam:
            tam=len(cad)
        elif tam!=len(cad):
            palindromos+=impar
            palindromos+=par
            par=[]
            impar=[]
            tam=len(cad)

        impar.append(int(cad+cad[::-1][1:]))
        par.append(int(cad+cad[::-1]))
    palindromos+=impar
    palindromos+=par
        
            
        
    