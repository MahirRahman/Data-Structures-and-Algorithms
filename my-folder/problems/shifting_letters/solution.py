class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        
    #Understand: Does the shift array have a number > 26 or number < 0?
    # % 26 ? 0 <= shifts[i] <= 109
    # Can the array be empty?  Cannot be empty
    
    # Sliding window
    # Helper func (shifting the letter)
    
    # 1 for loop
    # 
    # call helper function to get new chr? Put char as input
    # and the shift 
        prev = 0
        final_str = []
        for i in reversed(range(len(shifts))):
            prev += shifts[i]
            shifts[i] = prev
        for i in range(len(shifts)):
            final_str.append(self.shiftChar(s[i], shifts[i]))
        return ''.join(final_str)
            
    def shiftChar(self, ch, shift):
        shift = shift % 26
        ch = ord(ch) + shift
        if ch > ord('z'):
            ch = ch - ord('z') + ord('a') - 1
        return chr(ch)
        
            
                         
                    