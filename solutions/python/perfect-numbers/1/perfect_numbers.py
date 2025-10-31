def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")

    suma=sum(factores(number))

    if number==suma:
        return "perfect"

    if number<suma:
        return "abundant"

    return "deficient"

def factores(num):
    out=[]

    for pos in range(1,num):
        if num%pos==0:
            out.append(pos)

    return out
