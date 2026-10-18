class Solution:
    def countSeniors(self, details: List[str]) -> int:
        i = 0
       
        for word in details:
            age = int(word[11] + word[12])
            if age > 60:
                i = i + 1
            
        return i 
