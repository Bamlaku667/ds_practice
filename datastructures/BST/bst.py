# #different bst implementations 

# class Node: 
#     def __init__(self, key, left = None, right = None):
#         self.key = key
#         self.left = left
#         self.right = right


# class BST: 
#     root = None

#     #using iterative method 
#     def insert(self, key):
#         newNode = Node(key)
#         if self.root is None:
#             self.root = newNode
#             return 
#         prev_node = None
#         temp_node = self.root
#         while temp_node != None:
#             if newNode.key > temp_node.key:
#                 prev = temp_node
#                 temp_node = temp_node.right
#             elif newNode.key < temp_node.key:
#                 prev = temp_node
#                 temp_node = temp_node.left

#         if newNode.key < prev.key:
#             prev.left = newNode
#         else: 
#             prev.right = newNode

        
#     #iterative method of printing inorder

#     def inorder_iterative(self):
#         temp_node = self.root
#         stack = []
#         while (temp_node != None or len(stack) != 0):
#             if (temp_node != None):
#                 stack.append(temp_node)
#                 temp_node = temp_node.left
#             else:
#                 temp_node = stack.pop()
#                 print(temp_node.key, end = " ")
#                 temp_node = temp_node.right

#     # def search_tree(self, key):
#     #     result = self.search_utility(self.root, key)
#     #     if result is None:
#     #         print(f'{key} not found')
#     #     else: 
#     #         print(f"{key} found")
        
#     def search_utility(self, node, key):
        
#         if node is None or node.key == key:
#             return node
        
#         if node.key < key:
#             return self.search_utility(node.right, key)
         
#         return self.search_utility(node.left, key)
        

#     # delete a node with 2 child (inorder successor replacement)
#     # finding the smallest(minimum) node in the right part of the tree 
#     def delete_utility(self, node, key):
        

    




#     # #recursive method of printing inorder

#     # def inorder(self, node):
#     #     if node is not None:
            
#     #         self.inorder(node.left)
#     #         print(node.key , end = " ")
#     #         self.inorder(node.right)
#     # def print_inorder(self):
#     #     self.inorder(self.root)


#     def preorder(self, node):
#         if node is not None: 
#             print(node.key, end = " ")
#             self.preorder(node.left)
#             self.preorder(node.right)

#     def postorder(self, node):
#         node = self.root
#         if node is not None: 
#             self.postorder(node.left)
#             self.postorder(node.right)
#             print(node.key, end = " ")
            



    
    
# def main():
#     tree = BST()
#     tree.insert(50)

    
#     tree.insert(30) 
  
#     tree.insert(20) 
  
#     tree.insert(40) 
  
#     tree.insert(70) 
  
#     tree.insert(60) 
  
#     tree.insert(80) 


#     tree.inorder_iterative()
#     print()
#     tree.search_tree(79)

   


   

# if __name__ == "__main__":
#     main()
#     print()





class BST:
    def __init__(self, key , left = None, right = None) :
        self.key = key
        self.right = right
        self.left = left

    def pushNode(self, key):
        root = None:
        if 
        
        