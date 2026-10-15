class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            # skip if this fixed number is the same as the one before it
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1                # first spot after the fixed number
            r = len(nums) - 1        # last spot in the array

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l = l + 1        # need a bigger sum

                elif total > 0:
                    r = r - 1        # need a smaller sum

                else:
                    result.append([nums[l], nums[r], nums[i]])
                    l = l + 1        # move both pointers inward
                    r = r - 1

                    # skip repeated values for l so you don't add the same triplet again
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1

        return result