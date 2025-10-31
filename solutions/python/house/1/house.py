versos=[
    "the horse and the hound and the horn that belonged to",
    "the farmer sowing his corn that kept" ,
    "the rooster that crowed in the morn that woke",
    "the priest all shaven and shorn that married" ,
    "the man all tattered and torn that kissed" ,
    "the maiden all forlorn that milked",
    "the cow with the crumpled horn that tossed" ,
    "the dog that worried" ,
    "the cat that killed" ,
    "the rat that ate",
    "the malt that lay in",
    "the house that Jack built."
]

versos=versos[::-1]


def recite(start_verse, end_verse):
    out=[]
    for num_verso in range(start_verse-1,end_verse):
        out.append(verso(num_verso))

    [print(sal) for sal in out]
    return out

def verso(num):
    out=[]
    for num_verso in range(num+1):
        out.insert(0,versos[num_verso])
        
        
    return "This is "+" ".join(out)
        
