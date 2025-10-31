import math
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def __eq__(self, other):
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary

        if a==c and b==d:
            return True
        return False

    def __add__(self, other):
        a = self.real
        b = self.imaginary
        
        if isinstance(other,ComplexNumber):
            c = other.real
            d = other.imaginary
        else:
            c=other
            d=0

        real = (a + c)
        imaginary = (b + d)

        return ComplexNumber(real,imaginary)
        
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        otro=ComplexNumber(other,0)
        return otro-self

    def __rmul__(self, other):
        otro=ComplexNumber(other,0)
        return self*otro

    def __rtruediv__(self,other):
        otro=ComplexNumber(other,0)
        return otro/self
        

    def __mul__(self, other):
        a = self.real
        b = self.imaginary
        if isinstance(other,ComplexNumber):
            c = other.real
            d = other.imaginary
        else:
            c=other
            d=0

        real = (a * c - b * d)
        imaginary = (b * c + a * d)

        return ComplexNumber(real,imaginary)

    def __sub__(self, other):
        a = self.real
        b = self.imaginary
        if isinstance(other,ComplexNumber):
            c = other.real
            d = other.imaginary
        else:
            c=other
            d=0

        real = (a - c)
        imaginary = (b - d)

        return ComplexNumber(real,imaginary)

    def __truediv__(self, other):
        a = self.real
        b = self.imaginary
        
        if isinstance(other,ComplexNumber):
            c = other.real
            d = other.imaginary
        else:
            c=other
            d=0
        
        real = (a * c + b * d) / (c**2 + d**2)
        imaginary = (b * c - a * d) / (c**2 + d**2)

        return ComplexNumber(real,imaginary)

    def __abs__(self):
        return math.sqrt(self.real**2+self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real,-self.imaginary)

    def exp(self):
        a = self.real
        b = self.imaginary

        real = (math.e**a)*math.cos(b)
        imaginary = (math.e**a)*math.sin(b)

        return ComplexNumber(real,imaginary)
        
