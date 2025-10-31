import string,math
letras = list(string.ascii_lowercase)

def encode(plain_text, a, b):
    
    plain_text=plain_text.lower()
    string_out=""
    for letter in plain_text:
        if letter in letras:
            string_out+=encode_letter(letter,a,b)
        elif letter.isdigit():
            string_out+=letter
   
    return " ".join(string_out[pos:pos+5] for pos in range(0,len(string_out),5))


def decode(ciphered_text, a, b):
    if not is_coprime(a,b):
        raise ValueError("a and m must be coprime.")
    
    ciphered_text="".join([letter for letter in ciphered_text if letter!=" "])
    
    string_out=""
    for letter in ciphered_text:
        if letter in letras:
            string_out+=decode_letter(letter,a,b)
        elif letter.isdigit():
            string_out+=letter
    return string_out

def encode_letter(letter,a,b):
    if not is_coprime(a,len(letras)):
        raise ValueError("a and m must be coprime.")
    e_x=(a*letras.index(letter)+b)%len(letras)
    return letras[e_x]

def decode_letter(letter,a,b):
    if not is_coprime(a,len(letras)):
        raise ValueError("a and m must be coprime.")
    d_y=(pow(a, -1, len(letras)))*(letras.index(letter)-b)%len(letras)
    return letras[int(d_y)]

def is_coprime(a,b):
    if math.gcd(a, b)==1:
        return True
    return False
       
    
