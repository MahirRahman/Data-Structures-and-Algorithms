class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Boolean> map1 = new HashMap<Character, Boolean>();
        for (int i = 0; i < s.length(); i++) {
            if (map1.containsKey(s.charAt(i))) {
                map1.replace(s.charAt(i), false);
            }
            else {
                map1.put(s.charAt(i), true);
            }  
        }
        for (int i = 0; i < s.length(); i++) {
            if (map1.get(s.charAt(i)) == true) return i;
        }
        return -1;
    }
}