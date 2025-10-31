def find(search_list, value):
    inicio=0
    fin=len(search_list)-1
    


    while inicio<=fin:
        medio=(fin+inicio)//2
        if search_list[medio]==value:
            return medio

        if search_list[medio]>value:
            fin=medio-1
        else:
            inicio=medio+1

    raise ValueError("value not in array")