class Solution:
	# @param A : string
	# @return an integer
	def isValid(self, A):
        if len(A) % 2 != 0:
            return 0
        
        if len(A) == 0:
            return 0
            
            
        dict_characters =  {'}' : '{', ']':'[',')':'('}
        list_reverse_charcters = ['}',']',')']
        list_characters = []
        
        list_characters.append(A[0])
        
        for index in range(1,len(A)):
            if A[index] in list_reverse_charcters:
                if len(list_characters) !=0:
                    if list_characters[-1] == dict_characters[A[index]]:
                        list_characters.pop()
                    else:
                        return 0
                else:
                    return 0
            else:
                list_characters.append(A[index])
        
        
        if len(list_characters) != 0:
            return 0
        else:
            return 1
