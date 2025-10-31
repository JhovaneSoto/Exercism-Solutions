NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes=[]
        self.edges=[]
        self.attrs={}
        if data:
            if isinstance(data,list):
                if len(data[0])<3:
                    raise TypeError("Graph item incomplete")
                for item in data:
                    type_=item[0]
                    if type_==NODE:
                        self.make_node(item)
                        continue
                    if type_==EDGE:
                        self.make_edge(item)
                        continue
                    if type_==ATTR:
                        self.make_attrs(item)
                        continue
                    raise ValueError("Unknown item")
            else:
                raise TypeError("Graph data malformed")
        

    def make_node(self,item):
        if len(item)!=3:
            raise ValueError("Node is malformed")
        _,name,attrs=item
        node=Node(name,attrs)
        self.nodes.append(node)

    def make_edge(self,item):
        if len(item)!=4:
            raise ValueError("Edge is malformed")
        _,src,dst,attrs=item
        edge=Edge(src,dst,attrs)
        self.edges.append(edge)

    def make_attrs(self,item):
        if len(item)!=3:
            raise ValueError("Attribute is malformed")
        _,name,attrs=item
        self.attrs[name]=attrs