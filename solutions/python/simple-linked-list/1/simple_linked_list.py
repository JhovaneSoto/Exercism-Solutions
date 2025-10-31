class EmptyListException(Exception):
    def __init__(self,message):
        self.message=message


class Node:
    def __init__(self, value):
        self.valor=value
        self.siguiente=None
    def value(self):
        return self.valor

    def next(self):
        return self.siguiente


class LinkedList:
    def __init__(self, values=None):
        self.header=None
        if values:
            for value in values:
                nodo=Node(value)
                nodo.siguiente=self.header
                self.header=nodo

    def __iter__(self):
        actual=self.header
        while actual:
            yield actual.valor
            actual=actual.siguiente

    def __len__(self):
        return sum(1 for _ in self)

    def head(self):
        if self.header:
            return self.header
        raise EmptyListException("The list is empty.")

    def push(self, value):
        nodo=Node(value)
        nodo.siguiente=self.header
        self.header=nodo

    def pop(self):
        if len(self)==0:
            raise EmptyListException("The list is empty.")
        temp=self.header
        self.header=self.header.siguiente
        return temp.valor

    def reversed(self):
        return reversed([item for item in self])
