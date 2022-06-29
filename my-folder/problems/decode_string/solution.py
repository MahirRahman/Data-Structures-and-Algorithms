class Solution:
    def decodeString(self, s: str) -> str:
        stk = [["", 1]]
        k = 0
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stk.append(["", int(num)])
                num = ""
            elif c == ']':
                temp, x = stk.pop()
                stk[-1][0] += temp * x
            else:
                print(c)
                stk[-1][0] += c
        return stk[0][0]
                