class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        point = 0
        while point != 2 * len(nums): 
            
            ans.append(nums[ point % len(nums)])
            point = point + 1 
        
            
        return ans 

            
