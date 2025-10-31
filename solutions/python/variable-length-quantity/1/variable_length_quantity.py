def encode(numbers):
    list_out=[]
    for number in numbers:
        if number==0:
            list_out.append(0)
            continue
        out=[]
        #dividir en  segmentos
        
        while number>0:
            binario=number & 0x7F
            number>>=7
            out.append(bin(binario).replace("0b",""))
    
        #invertir lista
        out=out[::-1]
        for pos in range(len(out)):
            while len(out[pos])<7:
                out[pos]="0"+out[pos]
                
            if pos==len(out)-1:
                out[pos]="0"+out[pos]
            else:
                out[pos]="1"+out[pos]
            
            list_out.append(int(out[pos],2))
    return list_out

def decode(bytes_):
    out=[]
    num="0"
    binarios=[bin(item).replace("0b","") for item in bytes_]
    for pos,bite in enumerate(binarios):
        while len(bite)<8:
            bite="0"+bite
        print(bite)
        
        if bite[0]=="1":
            if pos==len(binarios)-1:
                raise ValueError("incomplete sequence")
            num+=bite[1:]
        else:
            num+=bite[1:]
            out.append(int(num,2))
            num="0"
    return out
