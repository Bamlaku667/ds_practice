#different bst implementations 

class Node: 
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right




def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node



def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key , end = " ")
        inorder(node.right)

def preorder(node):
    if node is not None: 
        print(node.key, end = " ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None: 
        postorder(node.left)
        postorder(node.right)
        print(node.key, end = " ")
        



    
    
def main():
    root = None
    root =  insert(root, 50)

    
    insert(root, 30) 
  
    insert(root, 20) 
  
    insert(root, 40) 
  
    insert(root, 70) 
  
    insert(root, 60) 
  
    insert(root, 80) 

    inorder(root)
    print()

    preorder(root)
    print()
    postorder(root)

if __name__ == "__main__":
    main()
    print()



        