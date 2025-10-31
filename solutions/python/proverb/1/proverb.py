base=["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
def proverb(*args,qualifier):
    *lista,=args
    if lista==[]:
        return []
    #dividir lista en pares
    out=[lista[pos:pos+2] for pos in range(0,len(lista)-1)]
    if len(out)==0 and len(lista)!=0:
        out.append([lista[0]])
    #convertir pares a texto
    salida=[]
    for par in out:
        if len(par)==2:
            salida.append(verso(par))

    if not qualifier:
        qualifier=""
    else:
        qualifier+=" "
    salida.append(f"And all for the want of a {qualifier}{out[0][0]}.")
    return salida

def verso(item):
    a,b=item
    return f"For want of a {a} the {b} was lost."