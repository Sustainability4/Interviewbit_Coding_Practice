# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        root = A  
        
        while A:
            if A.next and A.val == A.next.val :
                temp = A.next 
                A.next = A.next.next
                temp.next = None
                #A = A.next  # This was a big mistake, do make dry runs before you submit your code 
            else:
                A= A.next 
                
        return root 
