class Solution:
    def frequencySort(self, s: str) -> str:
        map = collections.Counter(s)
        heap = [(-v,k) for k,v in map.items()]
        heapq.heapify(heap)
        # d = {k: v for k, v in sorted(map.items(), key=lambda item: (item[1], item[0]), reverse=True)}
        res = []
        while heap:
            v,k = heappop(heap)
            for count in range(-v):
                res.append(k)
        # for k,v in d.items():
        #     for count in range(v):
        #         res.append(k)
        return ''.join(res)
                
            