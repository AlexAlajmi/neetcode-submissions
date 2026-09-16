class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Pass 1 (left to right): for each i, answer[i] should end up holding
        # the product of everything BEFORE index i.
        prefix = 1
        for i in range(n):
            answer[i] = prefix        # use `prefix` here
            prefix *= nums[i]            # update prefix to include nums[i]

        # Pass 2 (right to left): now fold in the product of everything AFTER
        # index i, multiplying it into what's already sitting in answer[i].
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i] 
        return answer     # combine