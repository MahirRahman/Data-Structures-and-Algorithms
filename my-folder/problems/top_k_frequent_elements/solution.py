class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        d={}
        result=[]
        for num in nums:
            d[num] = d.get(num,0)+1
        for key,v in d.items():
            arr[v].append(key)
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                result.append(n)
            if len(result) == k:
                return result
                    