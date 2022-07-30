class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lst = [True]
        for i in range(1, len(s) + 1):
            lst += any(lst[j] and s[j:i] in wordDict for j in range(i)),
            # if lst[-1] == False:
            #     return False
            # els
        # print(''.join(lst))
        # print(lst)
        return lst[-1]
            
            #     catsandog
            # lst -> cat, sand