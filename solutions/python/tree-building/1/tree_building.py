class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id
    def __repr__(self):
        return f"Record{(self.record_id,self.parent_id)}"


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    print(records)
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    #verificar si son validos los id
    if records:
        #si el ultimo id  es igual al tamaño de arreglo
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('Record id is invalid or out of order.')
        #si el primer id es igual a 0
        if ordered_id[0] != 0:
            raise ValueError('invalid')
            
    trees = []
    parent = {}
    #itera en las posiciones de los ID ordenados
    for i in range(len(ordered_id)):
        #destro de bucle itera en los records
        for j in records:
            #if el ID ordenado actual es igual al ID del record iterado
            if ordered_id[i] == j.record_id:
                #verifica si es ROOT valido
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError("Node parent_id should be smaller than it's record_id.")
                #valida si es valido el ID hijo respecto al padre
                if j.record_id < j.parent_id:
                    raise ValueError("Node parent_id should be smaller than it's record_id.")
                #valida si es igual el record y el parent ID, si es 0 se considera valido
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError('Only root should have equal record and parent id.')
                #se agrega el nodo
                trees.append(Node(ordered_id[i]))
                
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root
