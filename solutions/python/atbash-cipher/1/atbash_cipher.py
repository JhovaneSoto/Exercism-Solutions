letras="abcdefghijklmnopqrstuvwxyz"
numeros="0123456789"
def encode(plain_text):
    plain_text=plain_text.lower()
    out=""

    for pos,letra in enumerate(plain_text):
        if letra in letras:
            idx=letras.index(letra)
            out+=letras[::-1][idx]
        elif letra in numeros:
            out+=letra
    
    texto=list(out)
    secciones=[texto[num:num+5] for num in range(0,len(texto),5)]

    salida=[]
    for seccion in secciones:
        salida.append("".join(seccion))
    return " ".join(salida)

    


def decode(ciphered_text):
    ciphered_text=ciphered_text.replace(" ","")
    out=""

    for pos,letra in enumerate(ciphered_text):
        if letra in letras:
            idx=letras.index(letra)
            out+=letras[::-1][idx]
        elif letra in numeros:
            out+=letra

    return out
    
