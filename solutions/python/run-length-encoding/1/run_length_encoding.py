def decode(string):
    out=""
    cont=1
    last_digit=False
    for letter in string:
        if letter.isdigit():
            if last_digit:
                cont=cont*10+int(letter)
            else:
                cont=int(letter)
                last_digit=True
        else:
            print(cont)
            if last_digit:
                out+=letter*cont
            else:
                out+=letter
            last_digit=False
    print(out)
    return out


def encode(string):
    buffer=""
    cont=1
    out=""
    for letter in string:
        if letter!=buffer:
            if buffer!="":
                if cont>1:
                    out+=f"{cont}"
                out+=buffer
            buffer=letter
            cont=1
        else:
            cont+=1
            
    if buffer!="":
        if cont>1:
            out+=f"{cont}"
        out+=buffer
    return out