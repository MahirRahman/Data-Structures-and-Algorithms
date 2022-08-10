class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        curr = 1
        for i in range(len(nums)):
            result[i] *= curr
            curr *= nums[i]
        curr = 1
        for i in reversed(range(len(nums))):
            result[i] *= curr
            curr *= nums[i]
        return result