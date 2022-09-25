class Solution:
	# @param A : tuple of integers
	# @return an integer
    
	def longestConsecutive(self, A):
        A = list(set(list(A))) 
        # In order to understand that if there are repetitive elements then that should not be a problem
        # For e.g (1,1,2,2,3,3,4,4,10): Answer is 4 
        
        # Merge sort
        def merge(l,mid,h,list_):
            if h-l == 1:
                value_A = list_(l)
                if value_A > list_(h):
                    list_(l) = list_(h)
                    list_(h) = value_A
            
            i = l
            j = mid+1
            list__ = []
            while i in range(l,mid+1) and j in range(mid+1,h+1):
                
                if list_[i]<list_[j]:
                    list__.append(list_[i])
                    i = i+1
                    
                
                if list_[j]<list_[i]:
                    list__.append(list_[j])
                    j = j+1
                
                if list_[i] == list_[j]:
                    list__.append(list_[i])
                    list__.append(list_[j])
                    i = i+1
                    j = j+1
            
            while i in range(l,mid+1):
                list__.append(list_[i]) 
                i+=1
            
            while j in range(mid+1,h+1):
                list__.append(list_[j]) 
                j+=1   
                
            
            m = 0
            for k in range(l,h+1):
                list_[k] = list__[m]
                m = m+1
                
                
                
            
        def merge_sort(l,h,list_):
            if l==h:
                return 
            
            mid = int((l+h)/2)
            merge_sort(l,mid,list_)
            merge_sort(mid+1,h,list_)
            merge(l,mid,h,list_)
        
        
        A.sort()
        
        #print(A)
        
        index_element = A[0]
        consequetive_length = 1
        curr_length = 1
        for i in range(1,len(A)):
            if A[i]-index_element == 1 :
                curr_length = curr_length+1
                index_element = A[i]
            else:
                if curr_length > consequetive_length:
                    consequetive_length = curr_length
                curr_length = 1
                index_element = A[i]
        
        if curr_length>consequetive_length:
            consequetive_length = curr_length
            
        return consequetive_length
            
