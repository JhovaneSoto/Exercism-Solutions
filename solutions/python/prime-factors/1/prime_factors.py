def factors(value):
    factores=[]
    while value!=1:
        for number in range(2,value+1):
            if value%number==0:
                factores.append(number)
                value=value//number
                break

    return factores
