class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        greatest = 0
        for i in range(len(nums)):
            currNum = nums[i]
            result = 1
            if (currNum - 1 not in s):
                while (currNum + 1 in s):
                    result += 1
                    currNum += 1
                greatest = max(result, greatest)
        return greatest
