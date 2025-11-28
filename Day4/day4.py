class Solution(object):
    def isValid(self,s):
        
        stack=[]
        dict={'}':'{',']':'[',')':'('}

        for char in s:
            if char in dict:
                if not stack or stack[-1]!=dict[char]:
                    return False
            stack.pop()

            else:
                stack.append(char)


        if len(stack)==0:
            return True
        else:
            return False
