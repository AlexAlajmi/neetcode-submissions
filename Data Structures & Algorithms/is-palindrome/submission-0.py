class Solution(object):
    def isPalindrome(self, s):
        Sak = []
        for Char in s: 
            if Char.isalnum():
                Sak.append(Char.lower())
        if Sak == Sak[::-1]: 
            return True 
        else: 
            return False 
        