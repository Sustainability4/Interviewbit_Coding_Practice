
class Solution:
    # @param A : tuple of integers : (2,1,2)
    # @return an integer
    
    '''
    # Brute Force Solution 
    # Let's define the big O notation for this 
    def majorityElement(self, A):
        #self.A = A
        length = len(A)
        floor = int(length/2) # constant time K 
        
        list_unique_values = list(set(list(A)))
        
        max_element_value = 0
        max_element_frequency = 0
        list_A = list(A)
        
        for element in list_unique_values: # traversal m : number of unique values 
            count = 0
            for value in list_A: # traversal n  : length of the list 
                if element == value:
                    count = count+1

            if count > max_element_frequency: # comaprision : constant
                max_element_frequency = count
                max_element_value = element
                
        # Big O notation : O(mn) ~ O(n^2)
        
        if max_element_frequency > floor:
            return max_element_value
        else:
            return floor
    
    '''
    
    # Now one way is to sort the list and find out 
    
    def majorityElement(self, A):
        list_A = list(A)
        if len(list_A) == 1:
            return list_A[0]
        
        length = len(A)
        floor = int(length/2)
        
        
        list_A.sort() # Time Complexity O(log n)
        
        #print(list_A)
        count_value = list_A[0]
        value = 0
        frequency = 0
        count = 0
        
        for index in range(len(list_A)): # O(n) 
            element = list_A[index]
            if count_value == element: 
                count = count+1
            if count_value != element:
                if count > frequency:
                    frequency = count
                    value = list_A[index-1]
                count = 1
                count_value = element 
        
        # O(n) + O (log n)
        
        if frequency > floor:
            return value
        else:
            return list(A)[0]   
    
