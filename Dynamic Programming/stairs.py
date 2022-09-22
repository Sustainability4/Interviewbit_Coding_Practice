class Solution:
	# @param A : integer
	# @return an integer
    # Recursive Solution : I say that you bring me the answer of things if I just climb one step and answer of things if I climb two steps. Rest recurison will handle
    
    '''
	def climbStairs(self, A):
        
        def count_ways(n):
            if n == 0:
                return 1
            
            if n<0:
                return 0
                
            option_1 = count_ways(n-1) # O(n)
            option_2 = count_ways(n-2)
            
            return option_1 + option_2
            
        
        return count_ways(A)
        
    '''
    
    # Dynamic Programming : We try to avoid multiple calculations that we might be unnecessarily performing
    # In this case when we were recursively dealing with the problem we were trying to follow recursion more than we needed. 
    
    def climbStairs(self,A):
        
        def count_ways(dict_record, n):
            if n in list(dict_record.keys()):
                return dict_record[n]
                
            if n == 0:
                dict_record[n] = 1
                return 1
            
            if n<0:
                return 0
                
            option_1 = count_ways(dict_record,n-1)
            option_2 = count_ways(dict_record,n-2)
            
            dict_record[n] = option_1+option_2
            
            return option_1+option_2
            
        dict_record = {}
        
        return count_ways(dict_record,A)
    
    
