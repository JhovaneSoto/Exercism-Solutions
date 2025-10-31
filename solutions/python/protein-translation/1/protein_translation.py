codons = {
    "AUG"	:"Methionine",
    "UUU"	:"Phenylalanine",
    "UUC"	:"Phenylalanine",
    "UUA"   :"Leucine",
    "UUG"	:"Leucine",
    "UCU" 	:"Serine",
    "UCC" 	:"Serine",
    "UCA" 	:"Serine",
    "UCG"	:"Serine",
    "UAU"	:"Tyrosine",
    "UAC"	:"Tyrosine",
    "UGU"	:"Cysteine",
    "UGC"	:"Cysteine",
    "UGG"	:"Tryptophan",
    "UAA" 	:"STOP",
    "UAG"   :"STOP",
    "UGA"	:"STOP"
}

def proteins(strand):
    strand=[strand[num:num+3] for num in range(0,len(strand),3)]
    out=[]
    for codon in strand:
        acido=codons[codon]
        if acido=="STOP":
            return out
        else:
            out.append(acido)

    return out
    
