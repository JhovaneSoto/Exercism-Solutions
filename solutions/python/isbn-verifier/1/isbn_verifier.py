def is_valid(isbn):

    isbn=isbn.replace("-","")

    if len(isbn)!=10:
        return False

    if any([cad.isalpha() for cad in isbn[:len(isbn)-1]]):
        return False
    
        
    *resto,digit_10=isbn

    primeros_digitos="".join(resto)

    total=0
    cont=10
    for digito in primeros_digitos:
        total+=int(digito)*cont
        cont-=1

    if digit_10=="X":
        digit_10=10
    elif digit_10.isalpha():
        return False

    total+=int(digit_10)

    if total%11==0:
        return True
    return False

    
        
