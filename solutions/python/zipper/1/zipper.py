from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Context:
    direction: str
    parent_value: Any
    sibling_subtree: Optional[Any]

class Zipper:
    def __init__(self,tree,context=None):
        self.tree = tree
        self.context = context
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree["value"]

    def set_value(self,value):
        self.tree["value"]=value
        return Zipper(self.tree,self.context)

    def left(self):
        if not self.tree["left"]:
            return None
        context = Context(
            direction='left', 
            parent_value=self, 
            sibling_subtree=Zipper(self.tree["right"])
        )

        return Zipper(self.tree["left"],context)

    def set_left(self,rama):
        self.tree["left"]=rama
        return Zipper(self.tree,self.context)
        
    def right(self):
        if not self.tree["right"]:
            return None
        context = Context(
            direction='right', 
            parent_value=self, 
            sibling_subtree=Zipper(self.tree["left"])
        )
        return Zipper(self.tree["right"],context)

    def set_right(self,rama):
        self.tree["right"]=rama
        return Zipper(self.tree,self.context)

    def up(self):
        arbol = self.tree
        contexto = self.context
    
        if contexto:
            if contexto.direction == "left":
                arbol = {
                    "value": contexto.parent_value.tree["value"],
                    "left": arbol,
                    "right": contexto.sibling_subtree.tree if contexto.sibling_subtree else None
                }
            elif contexto.direction == "right":
                arbol = {
                    "value": contexto.parent_value.tree["value"],
                    "left": contexto.sibling_subtree.tree if contexto.sibling_subtree else None,
                    "right": arbol
                }
            contexto = contexto.parent_value.context
    
            return Zipper(arbol,contexto)
        return None
    def to_tree(self):
        arbol = self.tree
        contexto = self.context
    
        while contexto:
            if contexto.direction == "left":
                arbol = {
                    "value": contexto.parent_value.tree["value"],
                    "left": arbol,
                    "right": contexto.sibling_subtree.tree if contexto.sibling_subtree else None
                }
            elif contexto.direction == "right":
                arbol = {
                    "value": contexto.parent_value.tree["value"],
                    "left": contexto.sibling_subtree.tree if contexto.sibling_subtree else None,
                    "right": arbol
                }
            contexto = contexto.parent_value.context
    
        return arbol
