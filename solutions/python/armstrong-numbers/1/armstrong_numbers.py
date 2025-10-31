def is_armstrong_number(number):
    cad=str(number)

    pot=len(cad)

    tot=0

    for digito in cad:
        tot+=(int(digito)**pot)

    print(tot)

    if tot==number:
        return True
    return False
