class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        # while m > 0:
        #     nums1[m+n-1] = nums1[m-1]
        #     m-=1
        # while n > 0:
        #     nums1[m+n-1] = nums2[n-1]
        #     n-=1   
#         l = [nums1[i] for i in range(m)]
#         # print(l)
#         i = 0
#         j = 0
#         k = 0
#         while i < len(l) and j < len(nums2):
#             if l[i] <= nums2[j]:
#                 nums1[k] = l[i]
#                 i+=1
#             else:
#                 nums1[k] = nums2[j]
#                 j+=1
#             k+=1
#         while i < len(l):
#             nums1[k] = l[i]
#             k+=1
#             i+=1
#         while j < len(nums2):
#             nums1[k] = nums2[j]
#             k+=1
#             j+=1
        
                