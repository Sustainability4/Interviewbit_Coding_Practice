class Solution:
	# @param A : tuple of integers
	# @return an integer
    # The logic that I am thinking to try is about working on residuals 
    # If I obtain the first difference then I can add all the positive profits to obtain a total profit 
	def maxProfit(self, A):
        list_A = list(A)
        
        #initial_price = list_A[0]
        residual_list = []
        
        for i in range(1,len(list_A)):
            residual_list.append(list_A[i]-list_A[i-1])
        
        
        total_profit = 0    
        for profit in residual_list:
            if profit >0:
                total_profit = total_profit+profit
        
        return total_profit
