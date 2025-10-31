import re
class SgfTree:
    def __init__(self, properties=None, children=None):
        
        self.properties = properties or {}
        self.children = children or []
        

    @staticmethod
    def generate_node(string):
        pass
        
    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    print(input_string)
    if input_string == "(;)":
        return SgfTree(None,None)
    #1
    if not (input_string.startswith("(") and input_string.endswith(")")):
        raise ValueError("tree missing")
    if ";" not in input_string:
        raise ValueError("tree with no nodes")

    #2
    input_string = input_string [1:-1]
    idx = dot_comma_finder(input_string)
    
    properties_string = input_string
    children_string = ""
    
    if idx:
        properties_string = input_string[1:idx]
        children_string = input_string[idx:]
        
    #3
    idx_child = parentesis_finder(properties_string)

    child_parentesis = ""

    if idx_child:
        child_parentesis = properties_string[idx_child:]
        properties_string = properties_string[:idx_child]
    #5
    idx_properties = corchet_finder(properties_string)
        
    properties_values = []
    for pos in range(len(idx_properties)):
        next = pos+1
        if next >= len(idx_properties):
            properties_values.append(properties_string[idx_properties[pos]:])
        else:
            properties_values.append(properties_string[idx_properties[pos]:idx_properties[next]])

    print(properties_values)
            
    properties = None
    temp_properties = {}
    patron = r'\[((?:\\.|[^\]])*)\]'
    pat = r'([^\[\]]+)((?:\[(?:\\.|[^\]])*\])+]?)'
    
    if len(properties_values) == 0:
        raise ValueError("properties without delimiter")

    for item in properties_values:
        match = re.match(pat,item)
        if match:
            antes = match.group(1)
            if antes != antes.upper():
                raise ValueError("property must be in uppercase")

        
            all_values = re.findall(patron,match.group(2))
         
            for value in all_values:
                
                value = parse_text(value)
                if antes not in temp_properties.keys():
                    temp_properties[antes] = [value]
                else:
                    temp_properties[antes].append(value)
    
    if temp_properties != {}:
        properties = temp_properties

    children = None
    
    if len(children_string)>0:
        children = [parse(f"({children_string})")]

    if len(child_parentesis) > 0:
        children = []
        pat_2 = r'\([^()]*\)'
        for item in re.findall(pat_2,child_parentesis):
            children.append(parse(item))
    

    return SgfTree(properties,children)
    
def corchet_finder(cad):
    out = []
    for idx, letter in enumerate(cad):
        if letter == "[" and cad[idx-1] != "]":
            if idx - 2 < 0:
                out.append(idx-1)
            elif cad[idx-2] != "[":
                out.append(idx-1)
    return out

def parentesis_finder(cad):
    for idx, letter in enumerate(cad):
        if idx>0:
            if letter == "(" and (cad[idx-1] == "]" or cad[idx-1] == ")"):
                return idx
    return None
    
def dot_comma_finder(cad):
    for idx, letter in enumerate(cad):
        if idx>0:
            if letter == ";" and cad[idx-1] == "]":
                return idx
    return None


def parse_text(cad):
    
    if "\\\n" in cad:
        cad = cad.replace("\\\n","")

    
        
    if "\\\\" in cad:
        cad = cad.replace("\\\\","\\")
    elif "\\" in cad:
        cad = cad.replace("\\","")

    if "\]" in cad:
        cad = cad.replace("\]","]")

    cad = cad.replace("\t"," ")
    print("---")
    print(cad,"<---")
    return cad
#STEPS
#1 - Verificar la estructura de nodo corresponde a (;CONTENIDO)
#2 - Dividir internamente lo nodos dejando el primero como el principal
#3 - dividir las propiedades A[E]
#4 - Extraer variraciones
#5 - extraer valores
#6 - modificar cadenas