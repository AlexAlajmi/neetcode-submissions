class Solution:
    def isValid(self, s: str) -> bool:
        Open = {"{","[","("}
        Close = {"}","]",")"}
        matching = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s: 
            if char in Open:
                stack.append(char)
            else:
                if not stack:  # True when stack is empty
                    return False
                top = stack.pop()  # now safe to pop
                if top != matching[char]:
                    return False 
        if len(stack) > 0:
            return False 
        return True 
 