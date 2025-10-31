def can_chain(dominoes):
    out=ways_iterative(dominoes,len(dominoes)-1)
    if out == [[]]:
        return []
    out = [[item_2 for item_2 in item if isinstance(item_2,list)] for item in out]
    if out == [[]]:
        return []
    for candidate in out:
        if candidate[0][0]==candidate[-1][1]:
            return candidate

def ways_iterative(dominoes,lenght,last=None):
    #print(last,"-->",dominoes)
    
    if len(dominoes) == 0:
        return [[True]]
    blocks = dominoes.copy()
    
    out = []
    for block in blocks:
        n_block = list(block)
        idx_a = 0
        idx_b = 1
            
        if last:
            if last[1] in n_block:
                idx_a = n_block.index(last[1])
                idx_b = (idx_a + 1) % 2
            else:
                continue
        item = [n_block[idx_a],n_block[idx_b]]

        #blocks sin el actual
        temp_block = blocks.copy()
        temp_block.remove(block)
        otros = ways_iterative(temp_block,len(temp_block)-1,item)
        for otro in otros:
            out.append([item]+otro)
    return out

            
    