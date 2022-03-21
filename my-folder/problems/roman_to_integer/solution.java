
class Solution {
//     public String explanation(int number) {
        
//     }
//     public int romanToInt(String s) {
//         int total = 0;
//         for (int i = 0; i < s.length(); i++) {
            
//             if (s.charAt(i) == 'I') {
//                 if (i < s.length() - 1) {
//                     if (s.charAt(i + 1) == 'V') {
//                         total += 3;
//                         i++;
//                     }
//                     else if (s.charAt(i + 1) == 'X') {
//                         total += 8;
//                         i++;
//                     }
//                 }
//                 total += 1;
//             }
//             else if (s.charAt(i) == 'X') {
//                 if (i < s.length() - 1) {
//                     if (s.charAt(i + 1) == 'L') {
//                         total += 30;
//                         i++;
//                     }
//                     else if (s.charAt(i + 1) == 'C') {
//                         total += 80;
//                         i++;
//                     }
//                 }
//                 total += 10;
//             }
//             else if (s.charAt(i) == 'C') {
//                 if (i < s.length() - 1) {
//                     if (s.charAt(i + 1) == 'D') {
//                         total += 300;
//                         i++;
//                     }
//                     else if (s.charAt(i + 1) == 'M') {
//                         total += 800;
//                         i++;
//                     }
//                 }
//                 total += 100;
//             }
//             else if (s.charAt(i) == 'V') {
//                 total += 5;
//             }
//             else if (s.charAt(i) == 'L') {
//                 total += 50;
//             }
//             else if (s.charAt(i) == 'D') {
//                 total += 500;
//             }
//             else {
//                 total += 1000;
//             }
//         }
//         // String final = explanation(total);
//         return total;
//     }
    
    
    
    public static int romanToInt(String s) {
	if (s == null || s.length() == 0)
		return -1;
	HashMap<Character, Integer> map = new HashMap<Character, Integer>();
	map.put('I', 1);
	map.put('V', 5);
	map.put('X', 10);
	map.put('L', 50);
	map.put('C', 100);
	map.put('D', 500);
	map.put('M', 1000);
	int len = s.length(), result = map.get(s.charAt(len - 1));
	for (int i = len - 2; i >= 0; i--) {
		if (map.get(s.charAt(i)) >= map.get(s.charAt(i + 1)))
			result += map.get(s.charAt(i));
		else
			result -= map.get(s.charAt(i));
	}
	return result;
}
    
    
    
    
//     public int romanToInt(String s) {
//         int total = 0;
//         int prev = 0;
//         int index = -1;
//         char[] c = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
//         int[] vals = {1, 5, 10, 50, 100, 500, 1000};
        
//         for (int i = s.length() - 1; i >= 0; i--) {
//             for (int j = 0; j < 7; j++) if (c[j] == s.charAt(i)) index = j;
//             int curr = vals[index];
//             if (curr < prev) total -= curr;
//             else total += curr;
            
//             prev = curr;
//         }
        
//         return total;
//     }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}