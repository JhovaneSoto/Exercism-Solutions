def rows(row_count):
    if row_count<0:
        raise ValueError("number of rows is negative")
    if row_count==0:
        return []
    if row_count==1:
        return [[1]]
    else:
        anterior=rows(row_count-1)
        nueva=[]
        print(anterior[-1])
        for pos in range(row_count):
            inicio=pos-1
            if inicio<0:
                inicio=0
            fin=pos+1
            nueva.append(sum(anterior[-1][inicio:fin]))
        anterior.append(nueva)
    return anterior
