class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        #print(A)
        if len(A) == 1:
            return int(A[0])
        
        
        def operations(a,b,operator):
            if operator == "+":
                return a+b
            
            if operator == "-":
                return a-b
            
            if operator == "/":
                return int(a/b)
            
            if operator == "*":
                return a*b 
        
        
        list_characters = ["+", "-" , "*", "/"]
        # Easy way of doing this reversal : A.reverse()
        
        # queues for this purpose : first in first out 
        # In python a list can be used as a queue. 
        # A = [], A.append(a), A.append(b), A.append(c)
        # A.pop(0) everytime to use the first element 
        
        # We need to use stack for this purpose as we need to read 
        # the input in reverse order. 
        # A = [], A.append(a), A.append(b), A.append(c)
        # A.pop() to pop out last element 
        # List A can be used as a stack 
        
        value = 0
        index = 0
        
        while len(A) > 3:
            #print(A)
            while A[index] in list_characters:
                operator = A[index]
                a = A[index-2]
                b = A[index-1]
                #print(a,b,operator)
                sub_operation = operations(int(a),int(b),operator)
                A[index-2] = sub_operation
                #print(A[index-1])
                del A[index-1:index+1]
                #print(A)
                index = 0
                break
            
            index = index+1
        
        a = A[0]
        b = A[1]
        #print(a,b,A[2])
        #print(type(a), type(b), type(A[2]))
        #print(int(a), int(b))
        #print(A[2]=="/")
        final_value = operations(int(a),int(b),A[2])
        #print(final_value)
        
        return final_value
            
                
                
            
        
        
        
