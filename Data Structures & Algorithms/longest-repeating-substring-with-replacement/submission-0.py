class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        point = 0
        left = 0
        counts = {}
        maxLen = 0

        while point <= len(s) - 1:

            # add the new letter to the window
            counts[s[point]] = counts.get(s[point], 0) + 1
            

            # while the window needs more than k replacements, shrink it
            while point - left + 1 - max(counts.values()) > k  :
                counts[s[left]] = counts.get(s[left], 0) - 1       # lower the count of the letter leaving
                left = left + 1        # move left forward

            # window is valid now, check if it's the biggest so far
            if point - left + 1 > maxLen: 
                maxLen = point - left + 1

            point = point + 1

        return maxLen