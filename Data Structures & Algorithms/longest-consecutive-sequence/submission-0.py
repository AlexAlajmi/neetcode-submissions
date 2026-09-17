class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seet = set(nums)
        highestCount = 0 

        for num in seet: 
            if num - 1 not in seet:
                current_num = num
                current_count = 1
                while current_num + 1 in seet:
                    current_num += 1
                    current_count += 1
                highestCount = max(highestCount, current_count)
        return highestCount