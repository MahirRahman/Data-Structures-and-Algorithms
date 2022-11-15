class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        if len(set(words)) != len(set(pattern)):
            return False
        for i, word in enumerate(words):
            if word not in d:
                d[word] = pattern[i]
            elif d[word] != pattern[i]:
                    return False
        return True
            
            