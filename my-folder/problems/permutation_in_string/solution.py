class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f = {}
        for i in range(len(s1)):
            f[s1[i]] = f.get(s1[i],0)+1
        original = {}
        slow = 0
        i = 0
        while i < len(s1)-1:
            original[s2[i]] = original.get(s2[i],0)+1
            i+=1
        while i < len(s2):
            original[s2[i]] = original.get(s2[i],0)+1
            found=True
            for key,val in f.items():
                if key in original:
                    if val != original[key]:
                        found = False
                else:
                    found=False
            if found:
                return found
            else:
                original[s2[slow]] -= 1
            slow+=1
            i+=1
        print(f,original)
        return False