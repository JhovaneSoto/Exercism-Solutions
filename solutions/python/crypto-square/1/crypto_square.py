import math
def cipher_text(plain_text):
    plain_text="".join([letter.lower() for letter in plain_text if letter.isalpha() or letter.isdigit()])
    if len(plain_text)<2:
        return plain_text
    tam=len(plain_text)
    r,c=generate_r_c(tam)
    

    rectangle=[plain_text[pos:pos+c] for pos in range(0,tam,c)]
    
    for idx in range(len(rectangle)):
        while len(rectangle[idx])<c:
            rectangle[idx]+=" "
    out=[[] for _ in range(c)]
    
    for cadena in rectangle:
        for idx in range(len(cadena)):
            out[idx].append(cadena[idx])
    out=["".join(item) for item in out]
    return " ".join(out)
    
    
    

def generate_r_c(length):
    r=int(math.sqrt(length))
    c=math.ceil(length/r)
    while not(c - r <= 1):
        r+=1
        c=math.ceil(length/r)
    return r,c