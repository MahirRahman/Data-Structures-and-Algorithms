class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            low = i + 1
            high = len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == new_target:
                    return [i + 1, mid + 1]
                elif numbers[mid] > new_target:
                    high = mid - 1
                else:
                    low = mid + 1
            
                
            # def binarySearch(nums, target, low, high):
            #     if low > high:
            #         return -1
            #     mid = (low + high) // 2
            #     if nums[mid] == target:
            #         return mid
            #     elif nums[mid] > target:
            #         return binarySearch(nums, target, low, mid - 1)
            #     else:
            #         return binarySearch(nums, target, mid + 1, high)
            # index = binarySearch(numbers, new_target, 0, len(numbers) - 1)
            # if index != -1 and index != i:
            #     if index > i:
            #         return [i + 1, index + 1]
            #     else:
            #         return [index + 1,i + 1]
            