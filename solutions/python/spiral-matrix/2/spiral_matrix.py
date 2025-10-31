def spiral_matrix(size):
    out=[[None for _ in range(size)] for _ in range(size)]
    if size:
        delta_x, delta_y = 1,0
        x,y = 0,0
        
        for cont in range(size*size):
            out[y][x] = cont+1
            if not ([x+delta_x,y+delta_y] not in [[column,row] for row in range(len(out)) for column,data in enumerate(out[row]) if data] and (0<=x+delta_x<size and 0<=y+delta_y<size)):
                delta_x, delta_y = -delta_y, delta_x
            x += delta_x
            y += delta_y
    return out