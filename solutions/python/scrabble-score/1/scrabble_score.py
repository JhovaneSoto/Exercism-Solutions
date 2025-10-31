values={
    "A, E, I, O, U, L, N, R, S, T" : 1,
    "D, G" : 2,
    "B, C, M, P" : 3,
    "F, H, V, W, Y" : 4,
    "K" : 5,
    "J, X" : 8,
    "Q, Z" : 10
}
def score(word):
    word=word.upper()
    out=0
    for letra in word:
        for llaves in values.keys():
            if letra in llaves:
                out+=values[llaves]
                break
    return out
