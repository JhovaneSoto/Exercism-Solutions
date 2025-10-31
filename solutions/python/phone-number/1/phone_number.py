import re
class PhoneNumber:
    def __init__(self, number):


        if re.search(r"[a-zA-Z]",number):
            raise ValueError("letters not permitted")

        if re.search(r":",number):
            raise ValueError("punctuations not permitted")
       
        self.number=re.sub(r"[^0-9]", "", number)
        
        # if a phone number has less than 10 digits.
        if len(self.number)<10:
            raise ValueError("must not be fewer than 10 digits")
        
        # if a phone number has more than 11 digits.
        if len(self.number)>11:
            raise ValueError("must not be greater than 11 digits")
        
        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(self.number)==11 and not self.number.startswith("1"):
            raise ValueError("11 digits must start with 1")

        print(list(self.number))
        lista=list(self.number)
        *a,b,c,d,e,f,g,h,i,j=lista
        
        if d=="0":
            # if a phone number has an exchange code that starts with 0.
            raise ValueError("exchange code cannot start with zero")
        if d=="1":
            # if a phone number has an exchange code that starts with 1.
            raise ValueError("exchange code cannot start with one")
        if a[-1]=="0":
            # if a phone number has an area code that starts with 0.
            raise ValueError("area code cannot start with zero")

        if a[-1]=="1":
            # if a phone number has an area code that starts with 1.
            raise ValueError("area code cannot start with one")
        
        
        
        if len(lista)!=10:
            self.number="".join(lista[1:])
            self.area_code="".join(lista[1:4])
        else:
            self.area_code="".join(lista[:3])
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
