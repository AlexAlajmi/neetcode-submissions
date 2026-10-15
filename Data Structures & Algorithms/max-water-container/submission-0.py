class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1 
        maxWater = 0 


        while l < r: 
            if heights[l] < heights[r]:
                if heights[l] * (r - l) > maxWater: 
                    maxWater = heights[l] * (r - l)
                l = l + 1
            else:
                if heights[r] * (r - l) > maxWater: 
                    maxWater = heights[r] * (r - l)
                r =  r - 1
        return maxWater