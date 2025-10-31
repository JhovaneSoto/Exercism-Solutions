import math
def encode(message, rails):
    railes=["" for _ in range(rails)]
    delta=1
    rail=0
    for letter in message:
        railes[rail]+=letter
        if not 0<=rail+delta<rails:
            delta=-delta
        rail+=delta
    return "".join(railes)

def decode(encoded_message, rails):
    #tamaño de railes
    railes=["" for _ in range(rails)]
    delta=1
    rail=0
    for letter in encoded_message:
        railes[rail]+=letter
        if not 0<=rail+delta<rails:
            delta=-delta
        rail+=delta
    tamano=[len(item) for item in railes]

    #segment
    x=0
    railes=[]
    for pos in tamano:
        railes.append(list(encoded_message[x:x+pos]))
        x+=pos

    #string
    out=[]
    delta=1
    rail=0
    
    
    while any(item for item in railes):
        actual=railes[rail]
        out.append(actual[0])
        
        if not 0<=rail+delta<len(railes):
            delta=-delta
        railes[rail].pop(0)
        rail+=delta
    return "".join(out)
            