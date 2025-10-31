def append(list1, list2):
    return list1+list2


def concat(lists):
    return [item for elemento in lists for item in elemento]


def filter(function, list):
    return [elemento for elemento in list if function(elemento)]


def length(list):
    return len(list)


def map(function, list):
    return [function(elemento) for elemento in list]


def foldl(function, list, initial):
    actual=initial
    for item in list:
        actual=function(actual,item)

    return actual


def foldr(function, list, initial):
    actual=initial
    for item in list[::-1]:
        actual=function(actual,item)

    return actual


def reverse(list):
    return list[::-1]
