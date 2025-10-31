def flatten(iterable):
    salida=[]
    for item in iterable:
        if isinstance(item,list):
            salida+=flatten(item)
        elif item is not None:
            salida.append(item)

    return salida
