def is_isogram(string):

    string_letters="".join([letter.upper() for letter in string if letter.isalpha()])

    letras_unicas=set(string_letters)
    print(string_letters)
    print(letras_unicas)

    if len(string_letters)==len(letras_unicas):
        return True
    return False
