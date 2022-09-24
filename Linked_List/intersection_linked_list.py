# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    
    
    # Stored the node address in two lists and then found the first intersection of the lists 
    # There is no optimal Time complexity 
    # To resolve this we obtained the difference from the lists and then we made a point that we may travel
    # both the list together after eliminating the mutual difference
    def getIntersectionNode(self, A, B):
        list_A = []
        list_B = []
        
        while A: # O(n)
            list_A.append(A)
            #print(A.val)
            A = A.next
        
        while B : # O(n)
            list_B.append(B)
            #print(B.val)
            B = B.next
        
        #new_list = [value for value in list_A if value in list_B]
        
        #if len(new_list) >= 1:
            #return new_list[0]
            
        
        #if len(list_A)<= len(list_B):
            # O(n2)
            #for element in list_A:
                #if element in list_B:
                    #return element
            
        
        #if len(list_B)<len(list_A):
            #for element in list_B:
                #if element in list_A:
                    #return element
                    
        if len(list_A) <= len(list_B):
            diff = len(list_B)- len(list_A)
            index_A = 0
            index_B = diff
            while index_A<len(list_A) and index_B < len(list_B):
                if list_A[index_A] == list_B[index_B]:
                    return list_A[index_A]
                
                index_A = index_A+1
                index_B = index_B +1
        
        if len(list_A) > len(list_B):
            diff = len(list_A)- len(list_B)
            index_B = 0
            index_A = diff
            while index_A<len(list_A) and index_B < len(list_B):
                if list_A[index_A] == list_B[index_B]:
                    return list_A[index_A]
                
                index_A = index_A+1
                index_B = index_B +1
        
                    
        return None
        
    
    
    
        
