
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
        
        
     '''
    def majorityElement(self, A):
        list_A = list(A)
        if len(list_A) == 1:
            return list_A[0]
        
        length = len(A)
        floor = int(length/2)
        
        # Quick Sort 
        def quick_sort(list_A, i, j):
            if i >= j:
                return 
            
            if i+1 == j:
                if list_A[i]>list_A[j]:
                    lower = list_A[j]
                    list_A[j] - list_A[i]
                    list_A[i] = lower
                
                return list_A
            
            pivot = list_A[i]
            start_index = i
            end_index = j
            
            i = i+1
            
            while i<j:
                while list_A[i] <= pivot:
                    if i == end_index:
                        break
                    else:
                        i = i+1
                
                while list_A[j] > pivot:
                    if j == start_index:
                        break
                    else:
                        j = j-1
                        
                if i<j:
                    lower = list_A[j]
                    list_A[j] = list_A[i]
                    list_A[i] = lower
            
            
            lower = list_A[j]
            list_A[j] = list_A[start_index]
            list_A[start_index] = lower
            
            
            quick_sort(list_A,start_index,j-1)
            quick_sort(list_A, j+1, end_index)
            
            return list_A
        
        list_A = quick_sort(list_A, 0, length-1)
        
        count_value = list_A[0]
        value = 0
        frequency = 0
        count = 0
        
        for index in range(len(list_A)):
            element = list_A[index]
            if count_value == element: 
                count = count+1
            if count_value != element:
                if count > frequency:
                    frequency = count
                    value = list_A[index-1]
                count = 1
                count_value = element 
        
        if frequency > floor:
            return value
        else:
            return list(A)[0]
    '''    
    
