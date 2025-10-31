def square(number):
    return factorial(number)


def total():
    return factorial(64)*2-1


def factorial(num):
    if num>64 or num<1:
        raise ValueError("square must be between 1 and 64")
    tot=0
    for cant in range(num):
        if tot==0:
            tot=1
        else:
            tot*=2
    return tot