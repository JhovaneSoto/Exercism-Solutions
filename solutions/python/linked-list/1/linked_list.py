class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value=value
        self.succeeding=succeeding
        self.previous=previous
    def __repr__(self):
        return f"Node ({self.value},{self.succeeding},{self.previous})"


class LinkedList:
    def __init__(self):
        self.header=None
        
    def __iter__(self):
        nodo=self.header
        while nodo:
            yield nodo.value
            nodo=nodo.previous
            
    def __len__(self):
        print("- - - -")
        [print(value) for value in self]
        return sum(1 for _ in self)
    def push(self,value):
        nodo=Node(value)
        if self.header:
            self.header.succeeding=nodo
        nodo.previous=self.header
        self.header=nodo

    def pop(self):
        if not self.header:
            raise IndexError("List is empty")
        value=self.header.value
        self.header=self.header.previous
        return value
        
    def shift(self):
        if len(self)==0:
            raise IndexError("List is empty")
        if len(self)==1:
            return self.pop()
        nodo=self.header
        if nodo:
            while nodo.previous:
                nodo=nodo.previous
            if nodo.succeeding:
                nodo.succeeding.previous=None
            
            value=nodo.value
            return value
        
    def unshift(self,value):
        nodo=self.header
        if nodo:
            while nodo.previous:
                nodo=nodo.previous
    
            n_nodo=Node(value)
            n_nodo.succeeding=nodo
            nodo.previous=n_nodo
        else:
            self.push(value)
    def delete(self,value):
        nodo=self.header
        if nodo:
            
            while value!=nodo.value:
                nodo=nodo.previous
                if not nodo:
                    raise ValueError("Value not found")
            
            if value==nodo.value:
                
                if nodo.succeeding:
                    nodo.succeeding.previous=nodo.previous
                if nodo.previous:
                    nodo.previous.succeeding=nodo.succeeding
                if nodo==self.header:
                    if len(self)==1:
                        self.header=None
                    else:
                        self.header=nodo.previous
            else:
                raise ValueError("Value not found")
        else:
            raise ValueError("Value not found")
            
                