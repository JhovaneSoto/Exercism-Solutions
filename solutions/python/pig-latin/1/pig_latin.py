import re

def translate(text):
    return " ".join([convert_word(palabra) for palabra in text.split()])

def convert_word(word):
    salida=""
    
    #regla 1
    patron = r"([aeiou])(.*)"
    rule1=re.match(patron,word)
    
    if rule1 or word.startswith("xr") or word.startswith("yt"):
        return word+"ay"

    #regla 2
    patron = r"([^aeiou]+)(.*)"
    rule2=re.match(patron,word)
    
    if rule2:
        salida= rule2.group(2)+rule2.group(1)+"ay"

        
    #regla 3
    patron = r"([^aeiou]*qu)(.*)"
    rule3=re.match(patron,word)
    
    if rule3:
        salida= rule3.group(2)+rule3.group(1)+"ay"


    #regla 4
    patron = r"([^aeiou]+)y(.*)"
    rule3=re.match(patron,word)
    
    if rule3:
        print(rule3.group(1))
        print(rule3.group(2))
        salida = "y"+rule3.group(2)+rule3.group(1)+"ay"

    print(salida)
    

    

    

    return salida