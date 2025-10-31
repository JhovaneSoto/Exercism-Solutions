import copy
def total(basket):
    if basket==[]:
        return 0
    counter = {}

    for item in basket:
        if item in counter.keys():
            counter[item] += 1
        else:
            counter[item] = 1

    groups_num = max(counter[key] for key in counter.keys())
    counter_2 = counter.copy()
    lista_principal = groups_maker(counter, groups_num)
    
    lista_secundaria = groups_maker(counter_2, groups_num+1)
    
    minimo = None
    mini_item = []
    for item in lista_principal:
        temp_mini = evaluate_basket(item)
        if not minimo:
            minimo = temp_mini
            mini_item = item
        else:
            if temp_mini<minimo:
                minimo = temp_mini
                mini_item = item

    for item in lista_secundaria:
        if sum([num for row in item for elemento in item for num in elemento])==0:
            continue
        temp_mini = evaluate_basket(item)
        if not minimo:
            minimo = temp_mini
            mini_item = item
        else:
            if temp_mini<minimo:
                minimo = temp_mini
                mini_item = item
    #print(mini_item)
    return minimo
    
def evaluate_basket(basket):
    basket = [[item_2 for item_2 in item if item_2!=0] for item in basket]
    cont = 0
    for books in basket:
        num_book = len(books)
        cont_temp = num_book*800

        if num_book == 2:
            cont_temp *= 0.95
        if num_book == 3:
            cont_temp *= 0.90
        if num_book == 4:
            cont_temp *= 0.80
        if num_book == 5:
            cont_temp *= 0.75

        cont += cont_temp
            
        
    return cont
    

    
def groups_maker(counter,tam):
    if len(counter.keys())==0:
        return [[[] for _ in range(tam)]]

    main_key = list(counter.keys())[0]

    combi = combinations(main_key,counter[main_key],tam)
    #print(combi)
    out = []
    
    for item in combi:
        temp = [[] for _ in range(tam)]
        for idx, num in enumerate(item):
            temp[idx].append(num)
        out.append(temp)

    
    del counter[main_key]
    
    other = groups_maker(counter,tam)

    
    real_out = []
    for cesta_out in out:
        
        for cesta_other in other:
            temp_out = []
            #print(cesta_out,cesta_other)
            for idx, item in enumerate(cesta_other):
                temp_out.append(cesta_out[idx]+cesta_other[idx])
            real_out.append(temp_out)
    #print(real_out)
    return real_out
    
def combinations(num,counter,tam):
    if counter <= 0:
        return [[0 for item in range(tam)]]
    out = []
    
    for pos in range(tam-counter+1):
        temp_out = [0 for item in range(pos)]
        temp_out.append(num)
        
        otros = combinations(num,counter-1,tam-pos-1)
        for item in otros:
            out.append(temp_out+item)
    return out
 