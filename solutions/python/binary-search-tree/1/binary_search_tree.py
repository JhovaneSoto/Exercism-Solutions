class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
            
        


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree = TreeNode(tree_data[0])
        for item in tree_data[1:]:
            self.tree=self.find(self.tree,item)

    def find(self,nodo,item):
        if nodo is None:
            return TreeNode(item)
        else:
            if nodo.data<item:
                nodo.right=self.find(nodo.right,item)
            else:
                nodo.left=self.find(nodo.left,item)
        return nodo

    def data(self):
        return self.tree

    def sorted_data(self):
        return self.extract(self.tree)

    def extract(self,node):
        if node is None:
            return []
        else:
            left=self.extract(node.left)
            right=self.extract(node.right)
            return left+[node.data]+right
