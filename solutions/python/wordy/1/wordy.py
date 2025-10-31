def answer(question):
    #limpiar cadena
    question=question.replace("plus","+")
    question=question.strip("What is?")
    if es_entero(question):
        return int(question)

    question=question.split()
    question=[item for item in question if item!="by"]
    question=[int(item) if es_entero(item) else item for item in question]

    #sumas y restas
    idx=0
    while idx<len(question):
        try:
            if question[idx] in ["+","minus"]:
                if question[idx]=="+":
                    valor=question[idx-1]+question[idx+1]
                if question[idx]=="minus":
                    valor=question[idx-1]-question[idx+1]
                question.insert(idx+2,valor)
                question.pop(idx-1)
                question.pop(idx-1)
                question.pop(idx-1)
                idx=0
                continue
            idx+=1
        except Exception as e:
            print(e)
            raise ValueError("syntax error")


    #multiplicacion
    idx=0
    while idx<len(question):
        try:
            if question[idx] in ["multiplied","divided"]:
                if question[idx]=="multiplied":
                    valor=question[idx-1]*question[idx+1]
                if question[idx]=="divided":
                    valor=question[idx-1]/question[idx+1]
                question.insert(idx+2,valor)
                question.pop(idx-1)
                question.pop(idx-1)
                question.pop(idx-1)
                idx=0
                continue
            idx+=1
        except Exception as e:
            print(e)
            raise ValueError("syntax error")
            
            
    if len(question)==1:
        return question[0]
    else:
        lista_desconocida=[item for item in question if not es_entero(item)]
        if all([True if item in ["+","minus","divided","multiplied"] else False for item in  lista_desconocida ]):
            raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")
    
    



def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False