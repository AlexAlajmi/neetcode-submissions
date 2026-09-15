import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #I think what I want to do with this is make my list into Some sort 
        # of dictionary or some sort of hasmap 
        # I want to be able to see how many occurances we might see of certain Numbers 

        # Maybe I can sort then list then reurnt the k -1 

        #So first I am going to start off by creating a empty dict 
        seen = {}

        #now I want to create to create a for loop that is goign to load in this list and make into a dict 
        for value in nums: 
            if value in seen: 
                seen[value] += 1 
            else: 
                seen[value] = 1 
        top = heapq.nlargest(k, seen, key= seen.get)
        return top