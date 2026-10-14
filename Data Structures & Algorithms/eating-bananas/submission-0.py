class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_possible(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k   # hours for this pile at speed k (ceiling division)
            return hours <= h         # does the total fit in h?

        low = 1    # slowest possible speed
        high = max(piles)   # speed past which going faster changes nothing
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if is_possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans