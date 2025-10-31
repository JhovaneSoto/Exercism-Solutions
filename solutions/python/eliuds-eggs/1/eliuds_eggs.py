def egg_count(display_value):
    return sum(dec_binary(display_value))

def dec_binary(num):
    #definir num posiciones
    pos=1
    while 2**(pos-1)<num:
        pos+=1

    pos+=1

    #crear numero
    out=[]
    for pot in range(pos)[::-1]:
        if (2**pot)<=num:
            out.append(1)
            num-=(2**pot)
        else:
            out.append(0)

    return out