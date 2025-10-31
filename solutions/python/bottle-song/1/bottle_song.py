numero_en_ingles = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10:"ten"
}
def recite(start, take=1):
    out=[]
    out+=[item for pos in range(take) for item in create_verse(start-pos)]
    print(out)
    out.pop(-1)
    return out

def create_verse(pos):
    num=pos
    out=[]
    if num==1:
        out.append(f"{numero_en_ingles[num].capitalize()} green bottle hanging on the wall,")
        out.append(f"{numero_en_ingles[num].capitalize()} green bottle hanging on the wall,")
    else:
        out.append(f"{numero_en_ingles[num].capitalize()} green bottles hanging on the wall,")
        out.append(f"{numero_en_ingles[num].capitalize()} green bottles hanging on the wall,")

    out.append("And if one green bottle should accidentally fall,")
    if num-1 == 1:
        out.append(f"There'll be {numero_en_ingles[num-1]} green bottle hanging on the wall.")
    else:
        out.append(f"There'll be {numero_en_ingles[num-1]} green bottles hanging on the wall.")
    out.append("")
    return out
    