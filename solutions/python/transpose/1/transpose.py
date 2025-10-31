def transpose(text):
    columnas=text.split("\n")
    matriz=[list(letters) for letters in columnas]

    #maximo tam
    fila_tam=max([len(fila) for fila in matriz])

    #regular tamaño
    for idx in range(len(matriz)):
        while len(matriz[idx])<fila_tam:
            matriz[idx].append("_")

    #transponer
    out=[[] for _ in range(fila_tam)]
    
    for idx in range(len(matriz)):
        fila=matriz[idx]
        cont=0
        for idx_2,item in enumerate(fila):
            out[idx_2-cont].append(item)

    
    
    #convertir a cadena
    temp_lista=["".join(fila) for fila in out]
    temp_lista=[item.rstrip("_") for item in temp_lista]
    temp_lista=[item.replace("_"," ") for item in temp_lista]
    return "\n".join([fila for fila in temp_lista] )
    
    
