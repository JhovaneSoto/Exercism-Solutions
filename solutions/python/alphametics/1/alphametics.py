
import string

letters=list(string.ascii_uppercase)

def solve(puzzle):
    #define unique words
    words=puzzle.replace(" ","").split("=")
    words=[item for item in words if item!=""]
    
    sumas=words[0].split("+")
    c=words[1]

    words=[item for item in sumas if item!=""]
    
 

    unique=list(set( [letter for palabra in words for letter in palabra] +[letter for letter in c]))
    conf=valid_configuration(unique,words,c)

    dictionary={}
    for val,dat in zip(conf,unique):
        dictionary[dat]=val
    
    if dictionary=={}:
        return None

    for word in words:
        print(word,convert_cad(word,dictionary))
    print(c,convert_cad(c,dictionary))
    return dictionary

def valid_configuration(unique,words,c):
    lista=last_values(list(range(10)),len(unique))
    for item in lista:
        if verify_configuration(item,unique,words,c):
            return item
    return []

def verify_configuration(conf,unique,words,c):
    #make_dict

    dictionary={}
    for val,dat in zip(conf,unique):
        dictionary[dat]=val
    
    words_val = [convert_cad(cad,dictionary) for cad in words]

    
    c_val=convert_cad(c,dictionary)
    
    #if sum(words_val)==c_val:
        # print(dictionary)
        # print(words)
        # print(words_val)
        #print([len(words[pos]) == len(str(words_val[pos])) for pos in range(len(words_val))])
    
    return sum(words_val)==c_val and all([len(words[pos]) == len(str(words_val[pos])) for pos in range(len(words_val))]) and len(c) == len(str(c_val))

def convert_cad(cad,values):
    string_out=""
    for letter in cad:
        string_out+=str(values[letter])
    return int(string_out)

def last_values(lista,cont):
    if cont==0:
        return []
    out=[]
    for num in lista:
        n_list=lista.copy()
        n_list.remove(num)
        resto=last_values(n_list,cont-1)
        if resto!=[]:
            for item in resto:
                out.append([num]+item)
        else:
            out.append([num])
    return out


if __name__=="__main__":
    print(solve("AS + A == MOM"))