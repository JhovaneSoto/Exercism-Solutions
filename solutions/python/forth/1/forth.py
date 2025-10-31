import re
class StackUnderflowError(Exception):
    def __init__(self,message):
        self.message=message


def evaluate(input_data):
    input_data=[item.upper() for item in input_data]
    means={}
    for idx,item in enumerate(input_data):
        match=re.match(r": ([A-Z-+*]+) ([A-Z 0-9-+*]+) ;",item)
        if match:
            word=match.group(1)
            mean=match.group(2)
            mean_temp=[]
            for line in mean.split():
                
                if line in means.keys():
                    mean_temp.append(means[line])
                else:
                    mean_temp.append(line)
            means[word]=" ".join(mean_temp)
            continue
        
        
        for cad in item.split():
            if cad in means.keys():
                item=item.replace(cad,means[cad])
        input_data[idx]=item


            
        
            
    print(means)
    data = input_data[-1].upper().split()

    data=[int(item) if is_number(item) else item for item in data]
    cont=0
    while not(all([is_number(item) for item in data])) and cont<10:
        data=calculate_forth(data)
        cont+=1
        
    return data

def is_number(cad):
    try:
        int(cad)
        return True
    except:
        return False

def calculate_forth(data):
    print(data)
    while 1:
        for idx,item in enumerate(data):
            if not isinstance(item,int):
                if item == "+":
                    if idx < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    valor = data[idx-2]+data[idx-1]
                    data.pop(idx)
                    data.pop(idx-1)
                    data[idx-2] = valor
                    continue
                    
                if item == "-":
                    if idx < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    valor = data[idx-2]-data[idx-1]
                    data.pop(idx)
                    data.pop(idx-1)
                    data[idx-2] = valor
                    continue

                if item == "*":
                    if idx < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    valor = data[idx-2]*data[idx-1]
                    data.pop(idx)
                    data.pop(idx-1)
                    data[idx-2] = valor
                    continue

                if item == "/":
                    if idx < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    if data[idx-1]==0:
                        raise ZeroDivisionError("divide by zero")
                    valor = data[idx-2]//data[idx-1]
                    data.pop(idx)
                    data.pop(idx-1)
                    data[idx-2] = valor
                    continue
                if item == "DUP":
                    if idx < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    valor = data[idx-1]
                    data[idx] = valor
                    continue
                if item == "DROP":
                    if idx < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    data.pop(idx)
                    data.pop(idx-1)
                    continue

                if item == "SWAP":
                    if idx < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")

                    data[idx-2],data[idx-1]=data[idx-1],data[idx-2]
                    data.pop(idx)
                    continue

                if item == "OVER":
                    if idx < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")

                    data[idx] = data[idx-2]
                    continue
                print(item)
                if item=="FOO":
                    raise ValueError("undefined operation")
                raise ValueError("illegal operation")
        break
    return data
    
    
