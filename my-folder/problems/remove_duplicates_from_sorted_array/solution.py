class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        id = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[id] = nums[i]
                id+=1
        return id
                       
                
        
            