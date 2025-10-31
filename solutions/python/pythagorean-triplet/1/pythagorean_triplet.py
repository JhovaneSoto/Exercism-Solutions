import math
def triplets_with_sum(number):
    out=[]
    for a in range(number//3):
        for b in range(a+1,number//2):
            c=number-a-b
            if not(a<b<c):
                continue
            if not((a**2+b**2)==c**2):
                continue

            out.append([a,b,c])
            
    print(out)
    return out

def is_triplet(a,b,c,number):
    
    if not(a<b<c):
        return False
    if not((a**2+b**2)==c**2):
        return False
    return True