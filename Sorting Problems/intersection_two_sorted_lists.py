class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
    # Always put conditions in elif
	def intersect(self, A, B):
        
        list_A = list(A)
        list_B = list(B)
        
        list_intersection = []
        i = 0
        j = 0
        while i <len(list_A) and j <len(list_B):
            if list_A[i]< list_B[j]:
                i= i+1
            
            elif list_B[j]<list_A[i]:
                j=j+1
            
            elif list_B[j]==list_A[i]:
                #print(list_B[j])
                list_intersection.append(list_B[j])
                i=i+1
                j=j+1
        
        #print(list_intersection)
        
        return list_intersection
