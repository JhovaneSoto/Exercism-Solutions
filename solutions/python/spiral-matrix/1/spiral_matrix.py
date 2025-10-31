def spiral_matrix(size):
    out=[[None for _ in range(size)] for _ in range(size)]
    if size:
        sentido=[[1,0],[0,1],[-1,0],[0,-1]]
        x,y=0,0
        
        pasado=[]

        pos_sentido=0
        cont=1
        item=out[y][x]
        while not item:
            out[y][x]=cont
            cont+=1
            pasado.append([x,y])

            cambio=sentido[pos_sentido]

            if [x+cambio[0],y+cambio[1]] not in pasado and (0<=x+cambio[0]<size and 0<=y+cambio[1]<size):
                x+=cambio[0]
                y+=cambio[1]
            else:
                pos_sentido=(pos_sentido+1)%4
                cambio=sentido[pos_sentido]
                x+=cambio[0]
                y+=cambio[1]

            if all([item for row in out for item in row]):
                break
            item=out[y][x]
            
    return out
    
