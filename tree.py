class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def insert(node,x):
    if node==None:
        return Node(x)
    if node.data>x:
        node.left = insert(node.left,x)
    elif node.data<x:
        node.right = insert(node.right,x)
    return node

def search(node,x):
    if node.data==x:
        return True
    if node.data>x:
        node = search(node.left,x)
    elif node.data<x:
        node = search(node.right,x)
    return False

#通りがけ巡回
def traverse_h(node):
    if node is not None:
        traverse_h(node.left)
        print(node.data)
        traverse_h(node.right)

class Tree():
    def __init__(self):
        self.root=None
    def insert(self,x):
        self.root = insert(self.root,x)
    def search(self,x):
        return search(self.root,x)
tree = Tree()
data = [13,4,6,43]
for x in data:
    tree.insert(x)
print(tree.root.data)
traverse_h(tree.root)
