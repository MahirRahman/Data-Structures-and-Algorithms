class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        l = 0
        longest = 0
        for i in range(len(s)):
            if (d.get(s[i]) != None):
                l = max(l, d.get(s[i]) + 1)
            d[s[i]]= i
            longest = max(longest, i - l + 1)
        return longest

        