import re
pares = {
    '(': ')',
    '[': ']',
    '{': '}'
}
def is_paired(input_string):
    #limpiar_cadena
    brackets=r"[^()\[\]{}]"
    input_string=re.sub(brackets,"",input_string)

    #verificar
    last=""
    cola=[]
    for caracter in input_string:
        if caracter in pares.keys():
            cola.append(caracter)
            last=caracter
        else:
            if not last in pares.keys():
                return False
            if caracter!=pares[last]:
                return False
            else:
                cola.pop(-1)
                if len(cola)==0:
                    last=""
                else:
                    last=cola[-1]
    if len(cola)>0:
        return False
    return True
