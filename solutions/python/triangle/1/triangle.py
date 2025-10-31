def equilateral(sides):
    a,b,c=sides

    if is_triangle(sides) and a==b==c:
        return True
    return False


def isosceles(sides):
    sides.sort()
    a,b,c=sides
    if is_triangle(sides) and (a==b or b==c or a==c):
        return True
    return False

def scalene(sides):
    a,b,c=sides

    print(a!=b)
    print(b!=c)
    print(a!=c)
    print(is_triangle(sides))
    if is_triangle(sides) and (a!=b and b!=c and a!=c):
        return True
    return False

def is_triangle(sides):
    for side in sides:
        if side<=0:
            return False

    a,b,c=sides

    if (a+b>=c) and (a+c>=b) and (c+b>=a):
        return True
    return False
    