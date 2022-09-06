class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in s:
                size = 0
                while num+size in s:
                    size+=1
                longest = max(longest,size)
        return longest
                
                
                