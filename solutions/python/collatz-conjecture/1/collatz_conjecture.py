def steps(number):
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    contador=0

    while number!=1:
        if number%2==1:
            number=(number*3)+1
            contador+=1
        else:
            number=number//2
            contador+=1

    return contador


    
