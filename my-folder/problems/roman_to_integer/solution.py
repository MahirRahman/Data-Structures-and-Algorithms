class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500,"M":1000}
        result = roman[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            curr = roman[s[i]]
            next = roman[s[i + 1]]
            if (curr < next):
                result -= curr
            else: 
                result += curr
        return result