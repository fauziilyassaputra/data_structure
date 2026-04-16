r"""
komponen tree:
Root (akar)
child (cabang) -> anak root yang punya child lagi
leaf (daun) -> child yang tak punya cabang lagi
depth -> kedalaman data => root -> depth 0 
height -> ketinggian 'pohon'
subtree -> pecahan yang bisa menjadi root sendiri saat kepotong

binary tree -> yaitu maksimal 2 anak berupa left child dan right child



3 cara pemanggilan tree:
    - preorder
    - inorder
    - postorder

"""



class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def print_preorder(self,node):
        # base case
        if node:
            print(node.value)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_inorder(self,node):
        #basecase
        if node:
            self.print_inorder(node.left)
            print(node.value)
            self.print_inorder(node.right)

    def print_postorder(self,node):
        #basecase
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.value)

    


tree = BinaryTree()
tree.root = Node(10)
subtree1 = Node(20)
subtree1.left = Node(40)
subtree1.right = Node(50)

tree.root.left = subtree1
tree.root.right = Node(30)

"""
        10
       /  \
     20     30
     / \
    40  50

"""

print("Preorder Traversal")
tree.print_preorder(tree.root) # [10,20,40,50,30]


print("Inorder Traversal")
tree.print_inorder(tree.root) # [40,20,50,10,30]

print("postorder Traversal")
tree.print_postorder(tree.root) # [40,50,20,30,10]
