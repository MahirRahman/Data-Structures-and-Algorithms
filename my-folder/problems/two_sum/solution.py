class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            new_target = target - num
            if new_target in d:
                return [d[new_target], i]
            else:
                d[num] = i