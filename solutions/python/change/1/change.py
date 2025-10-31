def find_fewest_coins(coins, target):
    if target<0:
        raise ValueError("target can't be negative")
    if target == 0 or coins==[]:
        return []
        
    coins=sorted(coins,reverse=True)
    data=cambio(coins,target)
    out=data[target]
    if out==[]:
        raise ValueError("can't make target with given coins")
    
    return out
    

def cambio(coins,target):
    out=[[] for _ in range(target+1)]
    for pos in range(1,len(out)):
        soluciones=[]
        for coin in coins:
            count=pos-coin
            
            if count>=0:
                soluciones.append([coin])
                if count != 0:
                    soluciones[-1]+=out[count]
        try:
            soluciones=[item for item in soluciones if sum(item)==pos]
            out[pos]=sorted(min(soluciones,key=len))
        except:
            pass
    return out
                