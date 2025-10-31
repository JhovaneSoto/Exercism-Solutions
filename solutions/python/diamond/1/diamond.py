letras="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def rows(letter):
    idx=letras.index(letter)

    out=[]
    cont=idx

    for num in range(idx+1):
        if num==0:
            out.append(f"{' '*cont}{letras[num]}{' '*cont}")
        else:
            sep=(idx-cont)*2-1
            out.append(f"{' '*cont}{letras[num]}{' '*sep}{letras[num]}{' '*cont}")
        cont-=1

    out=out+out[:len(out)-1][::-1]
    print(out)
    return out
