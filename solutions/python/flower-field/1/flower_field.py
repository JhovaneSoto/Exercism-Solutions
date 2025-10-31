orientation=[
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1), 
    (-1, -1)
]
def annotate(garden):
    if not all([item in [" ","*"] for row in garden for item in row]):
        raise ValueError("The board is invalid with current input.")

    if garden:
        tam=len(garden[0])
        if not all([len(item)==tam for item in garden]):
            raise ValueError("The board is invalid with current input.")
    # Function body starts here
    out=[]
    for row in range(len(garden)):
        garden_row=""
        for column,item in enumerate(garden[row]):
            if item==" ":
                garden_row+=number_flowers(column,row,garden)
            else:
                garden_row+=item
        out.append(garden_row)
    return out

def number_flowers(column,row,garden):
    alto=len(garden)
    ancho=len(garden[0])

    cont=0
    for x,y in orientation:
        x+=column
        y+=row
        
        if 0<=x<ancho and 0<=y<alto:
            if garden[y][x]=="*":
                cont+=1
    if cont==0:
        return " "
    return str(cont)