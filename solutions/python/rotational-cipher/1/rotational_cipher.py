def rotate(text, key):
    if key==26:
        key=0

    #letras del abedecedario

    letras_may=[chr(num) for num in range(65,91)]
    letras_min=[chr(num) for num in range(97,123)]
        
    out=""

    for letter in text:
        if letter.isalpha():
            #dividir
            if letter in letras_may:
                idx=letras_may.index(letter)
                new_idx=idx+key
                if new_idx>=len(letras_may):
                    new_idx-=len(letras_may)

                out+=letras_may[new_idx]
            else:
                idx=letras_min.index(letter)
                new_idx=idx+key
                if new_idx>=len(letras_min):
                    new_idx-=len(letras_min)

                out+=letras_min[new_idx]    
        else:
            out+=letter

    return out
