def abbreviate(words):
    words=words.replace("-"," ")
    words=words.upper()
    words="".join([letter for letter in words if letter.isalpha() or letter ==" "])
    words=words.split()
    return "".join([letter[0] for letter in words])
