def commands(binary_str):

    comandos=[
        "wink", "double blink","close your eyes","jump",1
    ]
    out=[]

    for idx,code in enumerate(binary_str[::-1]):
        if code=="1":
            cadena=comandos[idx]
            if cadena==1:
                out=out[::-1]
            else:
                out.append(cadena)

    return out
