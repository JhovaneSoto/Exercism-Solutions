animals = [
    {"name": "fly"},
    {"name": "spider", "comment": "It wriggled and jiggled and tickled inside her.", "details": " that wriggled and jiggled and tickled inside her"},
    {"name": "bird", "comment": "How absurd to swallow a bird!"},
    {"name": "cat", "comment": "Imagine that, to swallow a cat!"},
    {"name": "dog", "comment": "What a hog, to swallow a dog!"},
    {"name": "goat", "comment": "Just opened her throat and swallowed a goat!"},
    {"name": "cow", "comment": "I don't know how she swallowed a cow!"},
    {"name": "horse", "comment": "She's dead, of course!"}
]

def recite(start_verse, end_verse):
    out=[]
    for verso in range(start_verse-1,end_verse):
        out+=generar_verso(verso)
        out.append("")
    if out[-1]=="":
        out.pop(-1)
    return out

def generar_verso(pos):
    out=[]
    item=animals[pos]
    out.append(f"I know an old lady who swallowed a {item['name']}.")
    for idx in range(pos,0,-1):
        item=animals[idx]
        if "comment" in item.keys() and idx==pos:
            out.append(item["comment"])
        if idx==7:
            return out
        if idx!=0:
            item_temp=animals[idx-1]
            if "details" in item_temp.keys():
                cad=f"She swallowed the {item['name']} to catch the {item_temp['name']}{item_temp['details']}."
            else:
                cad=f"She swallowed the {item['name']} to catch the {item_temp['name']}."
            out.append(cad)
    out.append("I don't know why she swallowed the fly. Perhaps she'll die.")
    return out
