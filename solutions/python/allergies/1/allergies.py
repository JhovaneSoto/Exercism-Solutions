alergias = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
}

class Allergies:

    def __init__(self, score):
        self.score=score
        self.allergics=[]
        if score>0:
            print("si")
            self.determinate_allergics()

    def allergic_to(self, item):
        return item in self.allergics

    def determinate_allergics(self):
        #potencia maxima de 2
        inicio=1
        while inicio<=self.score:
            inicio*=2

        #lista de potencias
        score=self.score
        marked=[]
        while score>0 and inicio>0:
            if inicio<=score:
                marked.append(inicio)
                score-=inicio
            inicio//=2

        #agregar alergias
        self.allergics=[alergias[item] for item in marked if item in alergias.keys()]

        
    @property
    def lst(self):
        return self.allergics
