import random
class Robot:
    names=[]
    def __init__(self):
        self.name=self.generate_name()
    def reset(self):
        self.name=self.generate_name()
        
    def generate_name(self):
        letras="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros="1234567890"
        
        palabra=""
        palabra+="".join(random.choice(letras) for _ in range(2))
        palabra+="".join(random.choice(numeros) for _ in range(3))
        
        while palabra in Robot.names:
            palabra=""
            palabra+="".join(random.choice(letras) for _ in range(2))
            palabra+="".join(random.choice(numeros) for _ in range(3))
        Robot.names.append(palabra)
        return palabra
