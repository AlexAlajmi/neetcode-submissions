class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        point = 0
        left = 0
        seen = set()
        maxLen = 0

        while point <= len(s) - 1:
            if s[point] not in seen:
                seen.add(s[point])
                if maxLen < len(seen):
                    maxLen = maxLen + 1
            else:
                while s[point] in seen:
                    seen.remove(s[left])
                    left = left + 1
                seen.add(s[point])
            point = point + 1
        return maxLen
            
            
