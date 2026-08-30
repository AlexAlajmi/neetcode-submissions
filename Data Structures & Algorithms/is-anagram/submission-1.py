class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter = {}
        t_letter = {}
        for char in s:
            s_letter[char] = s_letter.get(char, 0) + 1
        for char in t:
            t_letter[char] = t_letter.get(char, 0) + 1


        
        if s_letter == t_letter:
            return True
        else: 
            return False 
     