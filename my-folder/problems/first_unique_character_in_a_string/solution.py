class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for inx, ch in enumerate(s):
            if d[ch] == 1:
                return inx
        return -1