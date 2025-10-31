def convert(number):
    cad=""

    if number%3==0:
        cad+="Pling"

    if number%5==0:
        cad+="Plang"

    if number%7==0:
        cad+="Plong"

    if cad=="":
        return str(number)
    return cad
    
