abc="abcdefghijklmnopqrstuvwxyz"
import random
class Cipher:
    def __init__(self, key=None):
        if not key:
            self.key="".join([random.choice(abc) for _ in range(100)])
        else:
            self.key=key
        self.key_pos=[abc.index(letter) for letter in self.key]
        

    def encode(self, text):
        out=[]
        pos_key=0
        for letter in text:
            pos_original=abc.index(letter)
            pos_nueva=(self.key_pos[pos_key]+pos_original)%len(abc)
            out.append(abc[pos_nueva])
            pos_key=(pos_key+1)%len(self.key_pos)
            
        return "".join(out)
    def decode(self, text):
        out=[]
        pos_key=0
        for letter in text:
            pos_original=abc.index(letter)
            pos_nueva=(pos_original-self.key_pos[pos_key])%len(abc)
            out.append(abc[pos_nueva])
            pos_key=(pos_key+1)%len(self.key_pos)
        return "".join(out)
