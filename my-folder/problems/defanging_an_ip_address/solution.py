class Solution:
    def defangIPaddr(self, address: str) -> str:
        # final_str = []
        # for i in range(len(address)):
        #     if address[i] == ".":
        #         final_str.append("[.]")
        #     else:
        #         final_str.append(address[i])
        return '[.]'.join(address.split('.'))