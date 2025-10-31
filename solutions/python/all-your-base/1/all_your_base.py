def rebase(input_base, digits, output_base):
    if input_base<2:
        raise ValueError("input base must be >= 2")

    #verificar si son validos las bases

    for num in digits:
        if not(0<=num<input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base<2:
        raise ValueError("output base must be >= 2")

        
    #calcular valor real
    valor=base_valor(input_base,digits)
    print(valor)
    return valor_base(valor,output_base)

def base_valor(base,digitos):
    out=0
    for idx,num in enumerate(digitos[::-1]):
        out+=num*(base**idx)
    return out

def valor_base(valor,base):
    #definir el numero de posiciones que tendra la salida
    num_pos=1
    
    print("valor de base")
    
    while base_valor(base,[base-1]*num_pos)<valor:
        num_pos+=1

    print((base-1)*(base**(num_pos-1)))
    print(valor)
    print(num_pos)

    #agregar salida
    out=[]
    
    for pos in range(0,num_pos)[::-1]:
        ban=False
        for digito in range(0,base+1)[::-1]:
            if digito*(base**pos)<=valor:
                out.append(digito)
                valor-=digito*(base**pos)
                ban=True
                break
        if ban:
            continue
        out.append(0)
            
    print(out)
    return out
    

    