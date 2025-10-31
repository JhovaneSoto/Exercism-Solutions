def sum_of_multiples(limit, multiples):
    if any([True for num in multiples if num<0]):
        return 0
        
    suma=0
    salida=[]
    for multiplo in multiples:
        cont=1
        num=multiplo*cont
        while num<limit:
            salida.append(num)
            cont+=1
            num=multiplo*cont
            if num==0:
                break
            
    print(salida)
    salida=set(salida)
    suma=sum(salida)
            
    
    return suma
