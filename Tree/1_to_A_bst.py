# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        
        if A<1:
            return [None]
        
        if A == 1:
            node = TreeNode(A)
            return [node]
        
        def generate_bst(start,end):
            list_nodes = []
            
            if start>end:
                return [None]
            
            for i in range(start, end+1):
                leftsubnodes = generate_bst(start,i-1)
                rightsubnodes = generate_bst(i+1,end)
                
                for j in range(len(leftsubnodes)):
                    left = leftsubnodes[j]
                    for k in range(len(rightsubnodes)):
                        right = rightsubnodes[k]
                        
                        Node = TreeNode(i)
                        Node.left = left
                        Node.right = right
                        list_nodes.append(Node)
            
            return list_nodes
            
        return generate_bst(1,A)
      
      
 # post order traversal prints                        
