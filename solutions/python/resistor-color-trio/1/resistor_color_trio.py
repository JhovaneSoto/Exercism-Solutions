main_colors={
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def label(colors):
    *bandas,zeros=colors
    if len(bandas)>2:
        for color in range(2,len(bandas)):
            bandas[color]="black"
            
    valor="".join([str(main_colors[color]) for color in bandas])

    terminacion=""
    valor=str(int(valor))
    zeros=main_colors[zeros]
    
    valor+="0"*zeros

    print(valor)

    if "0"*9 in valor:
        valor=valor[::-1].replace("0"*9," gigaohms"[::-1] )
        valor=valor[::-1] 
    elif "0"*6 in valor:
        valor=valor[::-1].replace("0"*6," megaohms"[::-1])
        valor=valor[::-1]
    elif "0"*3 in valor:
        valor=valor[::-1].replace("0"*3," kiloohms"[::-1])
        valor=valor[::-1]
    else:
        valor+=" ohms"
        




    return valor
