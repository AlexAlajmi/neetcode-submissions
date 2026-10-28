class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0 
        intervals.sort(key =lambda x: x[1])
        prev = intervals[0]
        for interval in intervals[1:]: 
            if prev[1] <= interval[0]:
                prev = interval
            else:
                count = count + 1
        return count