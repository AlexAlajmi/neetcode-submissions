class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurances = dict(Counter(nums))
        for item, count in occurances.items(): 
            if count != 1:
                return True
         
        return False 