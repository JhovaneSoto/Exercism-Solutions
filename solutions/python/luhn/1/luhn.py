import re
class Luhn:
    def __init__(self, card_num):
        self.number=card_num

    def valid(self):
        #filtrar
        match=re.match(r"^[0-9\s]+$",self.number)
        if not match:
            return False

        numeros=[int(letra) for letra in self.number[::-1] if letra!=" "]
        if numeros==[0]:
            return False
        print(numeros)

        numeros_pros=[]
        for pos,numero in enumerate(numeros):
            if (pos+1)%2==0 and pos!=0:
                if numero*2>9:
                    numeros_pros.append((numero*2)-9)
                else:
                    numeros_pros.append(numero*2)
            else:
                numeros_pros.append(numero)

        print(numeros_pros)
        #suma
        suma=sum(numeros_pros)

        if suma%10==0:
            return True

        return False
            
        
