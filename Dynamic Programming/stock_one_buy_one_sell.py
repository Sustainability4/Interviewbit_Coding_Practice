class Solution:
	# @param A : tuple of integers
	# @return an integer
    # What its asking for is the maximum difference within a list. 
    # we will pickup one value from the list and sort all the remaining values and check the maximum difference 
    # This approach is not very time efficient 
    
    '''
	def maxProfit(self, A):
        
        
        list_A = list(A)
        
        if len(list_A) <= 1 or len(list(set(list_A))) <= 1:
            return 0
        
        
        max_diff = 0
        
        for i in range(0,len(list_A)):
            pivot_value = list_A[i]
            sub_list = list_A[i:]
            sub_list.sort()
            current_profit = sub_list[-1]-pivot_value
            
            if current_profit > max_diff :
                max_diff = current_profit
            
        
        return max_diff
    '''
    '''
    # lets try residual approach and add all the residuals till the last positive residuals 
    # Lets sort the list only once and then use that sorted list for all the future purposes
    def maxProfit(self, A):
        if len(A) <= 1:
            return 0
        
        list_A = list(A)
        list_A.sort() # O(logn)
        
        max_diff = 0
        for value in list(A): # O(n)
            
            if len(list_A) > 1:
                list_A.remove(value) 
                current_diff = list_A[-1] - value
            else:
                current_diff = 0
            
            if current_diff > max_diff:
                max_diff = current_diff
        
        
        return max_diff
    '''
    # O(n) solution for DP 
    def maxProfit(self, a):
        ans = 0
        localMinimum = 10 ** 8
        for i in range(len(a)):
            localMinimum = min(a[i], localMinimum)
            if a[i] - localMinimum > 0:
                ans = max(a[i] - localMinimum, ans)
        return ans
