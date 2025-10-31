def distance(strand_a, strand_b):
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return len([letter_a for letter_a,letter_b in zip(strand_a,strand_b) if letter_a!=letter_b])