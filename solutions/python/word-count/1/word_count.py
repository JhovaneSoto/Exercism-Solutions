import re
def count_words(sentence):
    sentence=re.sub(r"(?<![a-zA-Z])'|'(?![a-zA-Z])","",sentence)
    sentence=re.sub(r"[^a-zA-Z0-9']"," ",sentence)
    sentence=sentence.lower()
    data=[palabra for palabra in re.split(r"[:!?\s,]+", sentence) if palabra]
    unicos=set(data)
    out={}
    print(unicos)
    for unico in unicos:
        out[unico]=data.count(unico)

    return out
