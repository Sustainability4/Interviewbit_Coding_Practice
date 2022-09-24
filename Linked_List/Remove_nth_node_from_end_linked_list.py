# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        if B == 0:
            return A
        
        
        root = A 
        
        length_list = 0
        while A:
            length_list = length_list+1
            A = A.next 
        
        #print(length_list)
        if B == length_list:
            root = root.next 
            return root 
        
        if B > length_list:
            root = root.next
            return root
        
         
        A = root
        for i in range(length_list-B-1):
            A = A.next
        
        temp = A.next
        A.next = A.next.next
        temp.next = None 
        
        return root 
