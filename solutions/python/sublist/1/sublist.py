"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one==list_two:
        return EQUAL
    if is_sublist(list_one,list_two):
        return SUBLIST
    if is_sublist(list_two,list_one):
        return SUPERLIST
    return UNEQUAL


def is_sublist(sub,lista):
    tam_1,tam_2=len(lista),len(sub)

    for pos in range(tam_1-tam_2+1):
        if sub==lista[pos:pos+tam_2]:
            return True
    return False