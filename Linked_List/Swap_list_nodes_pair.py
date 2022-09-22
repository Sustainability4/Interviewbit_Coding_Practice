# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# What I am doing here is just swapping the values rather than swapping the entire node. 
# Although I copied this solution but this was owing to no experience in linked lists for me within python 
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
        
        root = A
        
        while(root and root.next):
            if root.val != root.next.val:
                root.val,root.next.val = root.next.val, root.val
            
            root = root.next.next
        
        return A
        
