class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n * n + n) / 2
        for num in nums:
            sum -= num
        return int(sum)