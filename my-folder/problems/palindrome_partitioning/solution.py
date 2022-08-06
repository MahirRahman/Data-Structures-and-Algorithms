class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(s):
            return s == s[::-1]
        def recurse(s, arr):
            if len(s) == 0:
                result.append(arr.copy())
                return
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    arr.append(s[0:i])
                    recurse(s[i:], arr)
                    arr.pop()
        recurse(s, [])
        return result
        
            
            
                
                
                