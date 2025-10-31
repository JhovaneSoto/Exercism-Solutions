romanos = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}
def roman(number):
    out=""
    while number!=0:
        for valor in romanos.keys():
            letter=romanos[valor]
            if valor<=number:
                out+=letter
                number-=valor
                break
    return out
                        
    
    
            

