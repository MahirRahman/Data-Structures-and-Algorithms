class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        length =0
        fast=0
        d = {}
        maxf = 0
        while fast < len(s):
            d[s[fast]] = d.get(s[fast],0)+1
            if maxf < d[s[fast]]:
                maxf=d[s[fast]]
            while (fast-slow+1) - maxf > k:
                d[s[slow]] -=1
                slow+=1
            length=max(fast-slow+1,length)
            fast+=1
        return length