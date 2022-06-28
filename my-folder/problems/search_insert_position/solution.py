class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)
        
    def binarySearch(self, nums, target, low, high):
        if low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, target, low, mid - 1)
            else:
                return self.binarySearch(nums, target, mid + 1, high)
        else:
            return low