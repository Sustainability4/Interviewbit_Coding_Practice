class Solution:
    # @param A : integer
    # @return a list of integers
    
    # For a Pascal's triangle : Sum of the entire row will be 2^k, first and last value is 1, second and 
    # second last value is the row number itself. Number of elements in thr row are equal to k+1
    
    def getRow(self, A):
        
        def get_pascal_row(k):
            if k == 0:
                return [0,1,0]
            
            list_k = []
            
            list_k.append(0)
            
            
            list_k_1 = get_pascal_row(k-1)
            
            for index in range(len(list_k_1)-1):
                sub_value = list_k_1[index] + list_k_1[index+1]
                list_k.append(sub_value)
                
            list_k.append(0)
            
            return list_k
        
        list_final = get_pascal_row(A)
        
        list_final.pop(0)
        list_final.pop()
        
        return list_final
            
