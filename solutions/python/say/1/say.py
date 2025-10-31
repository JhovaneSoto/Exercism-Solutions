numeros_en_ingles = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
def say(number):
    if number < 0:
        # if the number is negative
        raise ValueError("input out of range")
    if number > 999_999_999_999:
        # if the number is larger than 999,999,999,999
        raise ValueError("input out of range")

    if number in numeros_en_ingles.keys():
        return numeros_en_ingles[number]
        
    billion=0
    million=0
    thousand=0
    hundred=0
    out=[]
    
    if number>999_999_999:
        billion=number//1_000_000_000
        number=number-billion*1_000_000_000
        if billion:
            out.append(num_minor_999(billion)+" billion")
            
    if number>999_999:
        million=number//1_000_000
        number=number-million*1_000_000
        if million:
            out.append(num_minor_999(million)+" million")
            
    if number>999:
        thousand=number//1_000
        number=number-thousand*1_000
        if thousand:
            out.append(num_minor_999(thousand)+" thousand")
    
    
    if number:
        out.append(num_minor_999(number))

    return " ".join(out)

    
def num_minor_999(num):
    
    if num<100:
        return num_minor_99(num)
    else:
        centenas=num//100
        resto=num-centenas*100
        out=[]
        if centenas>0:
            out.append(num_minor_99(centenas)+" hundred")

        if resto>0:
            out.append(num_minor_99(resto))

        return " ".join(out)

def num_minor_99(num):
    if num in numeros_en_ingles.keys():
        return numeros_en_ingles[num]
    else:
        decenas=num//10
        resto=num-decenas*10
    
        out=[]
        if decenas>0:
            out.append(numeros_en_ingles[decenas*10])
            if resto>0:
                out.append(numeros_en_ingles[resto])
    
        return "-".join(out)

