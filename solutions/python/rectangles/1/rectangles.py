def rectangles(strings):
    
    if [item for string in strings for item in string].count("+")<4:
        return 0

    #limpiar vacios
    
    
    coords_tl=[]
    for row in range(len(strings)):
        for column,letter in enumerate(strings[row]):
            if letter=="+":
                coords_tl.append([column,row])
    limite_x=len(strings[0])
    limite_y=len(strings)
    #coords_tl son todas las esquinas
    cont=0
    for coord in coords_tl:
        cont+=num_rectagles(coord,coords_tl,limite_x,limite_y,strings)
    return cont
    
def num_rectagles(coord,coords_tl,lx,ly,strings):
    x_1,y_1=coord
    cont=0
    row=y_1

    for column in range(x_1+1,lx):
        if [column,row] in coords_tl and coord!=[row,column]:
            evaluate=[coord,[column,row]]
            evaluate_2=[]
            for item in coords_bottom(coords_tl,coord,[column,row],lx,ly):
                *lista,=*evaluate,*item
                evaluate_2.append(lista)
            for evaluate in evaluate_2:
                if len(evaluate)==4:
                    [a,b,c,d]=evaluate
                    
                    if is_rectagle(strings,a,b,c,d):
                        cont+=1
    return cont

def coords_bottom(coords_tl,coord_1,coord_2,lx,ly):
    x_1,y_1=coord_1
    x_2,y_2=coord_2
    
    out=[]
    for row in range(y_1+1,ly):
        if [x_1,row] in coords_tl and [x_2,row] in coords_tl:
            out.append([[x_2,row],[x_1,row]])
    return out
            
            
def is_rectagle(strings,coord_1,coord_2,coord_3,coord_4):
    if is_line(strings,coord_1,coord_2) and is_line(strings,coord_2,coord_3) and is_line(strings,coord_3,coord_4) and is_line(strings,coord_4,coord_1):
        return True
    return False
    
def is_line(strigs,coord_1,coord_2):
    linea=sorted([coord_1,coord_2],key=lambda x:(x[0],x[1]))
    x_1,y_1=linea[0]
    x_2,y_2=linea[1]
  
    if x_1==x_2:
        grupo=["+","|"]
    else:
        grupo=["-","+"]
    
    for row in range(y_1,y_2+1):
        for column in range(x_1,x_2+1):
            letter=strigs[row][column]
            if letter not in grupo:
                return False
    return True