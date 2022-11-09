class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
    
    def __lt__(self, nxt):
        if self.val != nxt.val:
            return self.val < nxt.val
        else:
            return self.key > nxt.key
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = collections.Counter(words)
        freqs = []
        heapify(freqs)
        for key,val in map.items():
            heappush(freqs, Node(key,val))
            if len(freqs) > k:
                heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs).key)
        return res[::-1]