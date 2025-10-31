from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.parent = None
        self.children = children if children is not None else []

        for children in self.children:
            children.parent = self

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        #find node
        node = find_node([self],from_node)
        if not node:
            raise ValueError("Tree could not be reoriented")
        return convert_tree(node)
    def path_to(self, from_node, to_node):
        
        node_main = self.from_pov(from_node)

        variations = []

        all_locations(node_main,variations,[])

        out = [item for item in variations if item[0] == from_node and item[-1] == to_node]

        if len(out) == 0:
            raise ValueError("No path found")

        return out[0]

def find_node(siblings, value):
    out = None
    for sibling in siblings:
        if sibling.label == value:
            out = sibling
            break
        other = None
        if sibling.children:
            other = find_node(sibling.children, value)
        if other:
            out = other
            break
    return out

def convert_tree(node,forbidden=[]):
    value = node.label
    children_data = []
    if node.parent:
        children_data.append(node.parent)
        
    children_data += node.children
    children_data = [item for item in children_data if item.label not in forbidden]
    
    

    children_out = []

    for children in children_data:
        children_out.append(convert_tree(children,forbidden+[value]))

    return Tree(value,children_out)

def all_locations(node, variations, cola):
    anterior = cola.copy()
    temp = anterior+[node.label]
    variations.append(temp)
    siblings_data = []
    for child in node.children:
        all_locations(child,variations,temp)
        

    