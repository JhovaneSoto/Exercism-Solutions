resistor_values={
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

resitor_tolerance={
    "grey" : "0.05%",
    "violet" : "0.1%",
    "blue" : "0.25%",
    "green" : "0.5%",
    "brown" : "1%",
    "red" : "2%",
    "gold" : "5%",
    "silver" : "10%"
}
def resistor_label(colors):
    while len(colors)<3:
        colors.append("black")
    *valores,mult,tolerancia=colors

    #definir valores
    value="".join([str(resistor_values[letter] )for letter in valores])
    value=str(int(value))

    #agregar multiplicador

    mult=resistor_values[mult]
    value+="0"*mult

    value=reemplazar_zeros(9,value," gigaohms")
    value=reemplazar_zeros(6,value," megaohms")
    value=reemplazar_zeros(3,value," kiloohms")

    if not "ohms" in value:
        value+=" ohms"

    if tolerancia in resitor_tolerance.keys():
        tole=f" ±{resitor_tolerance[tolerancia]}"
    else:
        tole=""
    return f"{value}{tole}"
    


def reemplazar_zeros(cant,cad,cad_reemplazo):
    
    if "0"*cant in cad:
        cad=cad[::-1].replace("0"*cant,cad_reemplazo[::-1])
        cad=cad[::-1]
    elif len(cad)>cant and not "ohms" in cad:
        cadena=list(cad)
        cadena.insert(-cant,".")
        cad="".join(cadena)
        cad=str(float(cad))+cad_reemplazo
    return cad

def colocar_punto(cad):
    num_zeros=cad.count("0")

    return 
    