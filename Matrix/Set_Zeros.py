class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        
        # setting rows and columns as zero 
        # We will set the row which contains zero as all zero and will also store 
        # the index at which that zero occurs 
        
        zero_index = []
        row_index = []
        for index_row in range(len(A)):
            row = A[index_row]
            if 0 in row:
                for index in range(len(row)):
                    if row[index] == 0 :
                        if index not in zero_index:
                            zero_index.append(index)
                    else:
                        row[index] = 0
            else:
                row_index.append(index_row)
        
        #print(row_index)
        #print(zero_index)
                
        if len(zero_index) !=0:    
            for index_1 in row_index:
                row = A[index_1]
                for index_2 in zero_index:
                    row[index_2] = 0
            
            
        return A
        
        
