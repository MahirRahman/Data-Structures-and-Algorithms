class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def findMinMax(l,r):
            min = float("inf")
            max = float("-inf")
            for i in range(l,r):
                if nums[i] < min:
                    min = nums[i]
                if nums[i] > max:
                    max = nums[i]
            return min,max
        if len(nums) < 2:
            return 0
        start,end=0,len(nums) - 1
        while start < len(nums) - 1 and nums[start] <= nums[start + 1]:
            start += 1
        while end > 0 and nums[end - 1] <= nums[end]:
            end -= 1
        if start > end:
            return 0
        # print(start,end)
        tempMin, tempMax = findMinMax(start,end+1)
        while start > 0 and tempMin < nums[start-1]:
            start -= 1
        while end < len(nums) - 1 and tempMax > nums[end+1]:
            end += 1
        return end - start + 1