import math
class Rational:
    def __init__(self, numer, denom):
        numer=int(numer)
        denom=int(denom)
        for divisor in range(max([numer,denom]),1,-1):
            if numer%divisor == 0 and denom%divisor == 0:
                numer /= divisor
                denom /= divisor
        if denom<0:
            denom*=-1
            numer*=-1
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        numer = (self.numer*other.denom)+(other.numer*self.denom)
        denom = self.denom*other.denom
        
        return Rational(numer,denom)

    def __sub__(self, other):
        numer = (self.numer*other.denom)-(other.numer*self.denom)
        denom = self.denom*other.denom
        
        return Rational(numer,denom)

    def __mul__(self, other):
        numer = self.numer*other.numer
        denom = self.denom*other.denom
        
        return Rational(numer,denom)

    def __truediv__(self, other):
        numer = self.numer*other.denom
        denom = self.denom*other.numer
        
        return Rational(numer,denom)

    def __abs__(self):
        return Rational(abs(self.numer),abs(self.denom))

    def __pow__(self, power):
        if power>0:
            numer = self.numer**power
            denom = self.denom**power
        else:
            power=abs(power)
            numer = self.denom**power
            denom = self.numer**power

        print(Rational(numer,denom))
        return Rational(numer,denom)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)