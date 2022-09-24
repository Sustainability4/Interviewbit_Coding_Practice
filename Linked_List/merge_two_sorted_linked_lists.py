# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    
    '''
    # We kept storing values in a list depending upon the sorted order for both the combined linked lists 
    # Time Complexity was O(n+m) where n is length of linked list A and m is length of linked list B 
    
    # But in this solution there is a space complexity which can be reduced. 
    
	def mergeTwoLists(self, A, B):
        list_number = []
        
        while A and B:
            if A.val == B.val:
                list_number.append(A.val)
                list_number.append(B.val)
                A = A.next 
                B = B.next 
            
            elif A.val > B.val:
                list_number.append(B.val)
                B = B.next 
            
            elif B.val> A.val:
                list_number.append(A.val)
                A = A.next
                
            
        if A == None and B != None:
            while B :
                list_number.append(B.val)
                B = B.next
        
        if A!= None and B == None:
            while A:
                list_number.append(A.val)
                A = A.next 
        
        root = ListNode(list_number[0])
        
        temp = root 
        
        for i in range(1,len(list_number)):
            temp.next = ListNode(list_number[i])
            temp = temp.next 
        
        return root 
    
    '''
    
    # Very interesting O(1) space compelxity solution : Revise this one 
    def mergeTwoLists(self, A, B):
        master = B
        minion = A
        
        if A.val<= B.val:
            master = A
            minion = B
        
        curr = master 
        
        while minion is not None:
            while curr.next and curr.next.val <= minion.val:
                curr = curr.next
            
            mNext = minion.next
            minion.next = curr.next
            curr.next = minion
            minion = mNext
            
        return master     
