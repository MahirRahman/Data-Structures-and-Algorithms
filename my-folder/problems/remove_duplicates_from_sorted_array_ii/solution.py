class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        id = 2
        for i in range(2,len(nums)):
            if nums[i] > nums[id-2]:
                nums[id] = nums[i]
                id += 1
        return id