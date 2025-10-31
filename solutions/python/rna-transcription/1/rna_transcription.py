def to_rna(dna_strand):
    return "".join([change(letter) for letter in dna_strand])

def change(letter):
    if letter=="G":
        return "C"

    if letter=="C":
        return "G"
        
    if letter=="T":
        return "A"

    if letter=="A":
        return "U"

    return letter
