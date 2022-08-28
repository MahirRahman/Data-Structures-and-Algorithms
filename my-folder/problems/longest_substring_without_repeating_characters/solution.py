class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedChar = {}
        length, start = 0, 0
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                length = max(length, i - start + 1)
            usedChar[s[i]] = i
            
        return length