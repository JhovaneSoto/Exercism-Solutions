h_cards={
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}

def best_hands(hands):
    manos=[mano.split() for mano in hands]
    if len(manos)==1:
        return [" ".join(manos[0])]
    values=[[valor_mano(mano),mano] for mano in manos]

    #extraer el mayor
    puntos=[0,0,0]
    mano_out=[]
    for valor in values:
        print(valor)
        [a,b,c],mano=valor
        
        [tipo,punto_a,punto_b]=puntos
        
        if a>tipo:
            mano_out=[mano]
            puntos=[a,b,c]
            
        if a==tipo and b>punto_a:
            mano_out=[mano]
            puntos=[a,b,c]
            
        if a==tipo and b==punto_a:
            if punto_b<c:
                mano_out=[mano]
            elif punto_b==c:
                mano_out.append(mano)
                
    if len(mano_out)>1:
        mano_out=carta_alta_baja(mano_out)
    return [" ".join(mano) for mano in mano_out]
            


def carta_alta_baja(datos):
    manos=[]
    for dato in datos:
        mano=[]
        for item in dato:
            *a,b=item
            a="".join(a)
            if a in h_cards.keys():
                a=h_cards[a]
            a=int(a)
            mano.append([a,b])
        manos.append(sorted(mano,key=lambda x:(x[0]),reverse=True))
        
    indices_win=list(range(len(manos)))[::-1]
    #iterar en las 5 cartas
    for idx_card in range(5):
        max_carta=max(manos[idx][idx_card][0] for idx in indices_win)
        for idx in indices_win:
            if manos[idx][idx_card][0]!=max_carta:
                indices_win.remove(idx)
               
                
    indices_win=indices_win[::-1]
    
    return [datos[idx] for idx in indices_win]

    
    
def valor_mano(dato):
    mano=[]
    for item in dato:
        *a,b=item
        a="".join(a)
        if a in h_cards.keys():
            a=h_cards[a]
        a=int(a)
        mano.append([a,b])
    
    valor_set=set([item[0] for item in mano])
    palo_set=set([item[1] for item in mano])
    #Royal Flush (Escalera Real)
    if len(palo_set)==1:
        valor_ordenado=sorted(list(valor_set))
        if valor_ordenado[2]==(sum(valor_ordenado)/5):
            return [10,sum(valor_ordenado),0]
        if 14 in valor_ordenado:
            valor_ordenado=sorted([1 if num==14 else num for num in valor_ordenado])
            if valor_ordenado[2]==(sum(valor_ordenado)/5):
                return [10,sum(valor_ordenado),0]
        
    #Straight Flush (Escalera de Color) & COLOR
    if len(valor_set)==5 and len(palo_set)==1:
        valor_ordenado=sorted(list(valor_set))
        if valor_ordenado[2]==(sum(valor_ordenado)/5):
            return [9,sum(valor_ordenado),0]
        else:
            return [6,sum(valor_ordenado),0]

    #Four of a Kind (Póker / Cuatro iguales)
    if any([True if [item[0] for item in mano].count(item2)==4 else False for item2 in list(valor_set)]):
        return [8,sum([item2 if [item[0] for item in mano].count(item2)==4 else False for item2 in list(valor_set)]*4),0]

    #Full House (Full / Casa llena)
    if all([True  if [item[0] for item in mano].count(item2) in [2,3] else False for item2 in list(valor_set)]):
        
        return [7,sum([item for item in list(valor_set) if [item[0] for item in mano].count(item)==3]),0]

    #Straight (Escalera)
    if len(valor_set)==5:
        valor_ordenado=sorted(list(valor_set))
        if valor_ordenado[2]==(sum(valor_ordenado)/5):
            return [5,sum(valor_ordenado),0]
        if 14 in valor_ordenado:
            valor_ordenado=sorted([1 if num==14 else num for num in valor_ordenado])
            if valor_ordenado[2]==(sum(valor_ordenado)/5):
                return [5,sum(valor_ordenado),0]

    #Trio
    if any([True if [item[0] for item in mano].count(item2)==3 else False for item2 in list(valor_set)]):
        return [4,sum([item2 if [item[0] for item in mano].count(item2)==3 else False for item2 in list(valor_set)*3]),0]

    #Par doble
    if len([True for item2 in list(valor_set) if [item[0] for item in mano].count(item2)==2])==2:
        return [3,0,0]
        
    #Par
    if any([True for item2 in list(valor_set) if [item[0] for item in mano].count(item2)==2]):
        #sum([item2 for item2 in list(valor_set) if [item[0] for item in mano].count(item2)==2]*2)
        return [2,sum([item2 for item2 in list(valor_set) if [item[0] for item in mano].count(item2)==2]*2),0]
    return [1,max(list(valor_set)),sum([item[0] for item in mano])]

    
    