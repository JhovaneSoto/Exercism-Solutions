def square_root(number):
    inicio=1
    fin=number
    while inicio<fin:
        medio=(inicio+fin)//2

        resultado=medio*medio
        if resultado==number:
            return medio

        if resultado>number:
            fin=medio-1

        if resultado<number:
            inicio=medio+1

    return inicio
