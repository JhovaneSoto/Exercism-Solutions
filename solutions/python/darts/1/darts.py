def score(x, y):

    pos=distancia(x,y)

    if pos>10:
        return 0

    if pos>5:
        return 1

    if pos>1:
        return 5

    return 10


def distancia(x,y):
    return (x**2+y**2)**0.5