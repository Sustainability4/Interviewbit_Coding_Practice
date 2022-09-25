class Solution:
	# @param A : integer
	# @return an integer
    
    # Simple way of doing this with inbuilt python functions
    '''
	def isPalindrome(self, A):
        
        if A < 0:
            return 0
        
        str_A = str(A)
        
        if str_A == str_A[::-1]:
            return 1
        else:
            return 0
    '''
    
    def isPalindrome(self, A):
        
        if A<10 and A>=0:
            return 1
        
        if A < 0:
            return 0
        
        list_A = []
        i = 1
        while A > 10**i:
            remainder = A%(10**i)
            remainder = remainder//(10**(i-1))
            
            list_A.append(remainder)
            i = i+1
        
        remainder = A%(10**i)
        remainder = remainder//(10**(i-1))
            
        list_A.append(remainder)
        
        reverse_number = 0
        
        length = i
        while i>0:
            value = list_A[length-i]
            reverse_number = reverse_number + value*(10**(i-1))
            i = i-1
        
        if reverse_number == A:
            return 1
        else:
            return 0
            
            
    
