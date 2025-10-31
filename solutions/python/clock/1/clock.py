from datetime import datetime
class Clock:
    def __init__(self, hour, minute):
        self.hour=0
        self.minute=0
        self.actualizar_hora(hour,minute)
        

    def __repr__(self):
        return f"Clock{self.hour,self.minute}"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if self.hour==other.hour and self.minute==other.minute:
            return True
        return False

    def __add__(self, minutes):
        self.actualizar_hora(0,minutes)
        return self.__str__()

    def __sub__(self, minutes):
        self.actualizar_hora(0,-minutes)
        return self.__str__()

    def actualizar_hora(self,hora,minutos):
        self.minute+=minutos
        hora+=(self.minute//60)
        self.hour+=hora
        self.hour=self.hour%24
        self.minute=self.minute%60
