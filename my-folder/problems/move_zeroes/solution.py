class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast= 0
        for slow in range(len(nums)):
            if nums[slow] == 0:
                if fast < slow:
                    fast = slow + 1
                while fast < len(nums) and nums[fast] == 0:
                    fast+=1
                if fast == len(nums):
                    return
                nums[slow] = nums[fast]
                nums[fast] = 0