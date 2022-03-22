class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        // int index = 0;
        // if (magazine.length() < ransomNote.length()) return false;
        // while (index < ransomNote.length()) {
        //     char need = ransomNote.charAt(index++);
        //     boolean found = false;
        //     for (int i = 0; i < magazine.length(); i++) {
        //         if (need == magazine.charAt(i)) {
        //             magazine = magazine.substring(0, i) + magazine.substring(i + 1, magazine.length());
        //             found = true;
        //             break;
        //         }
        //     }
        //     if (found == false) return false;
        // }
        // return true;
        
        int[] arr = new int[26];
        
        for (int i = 0; i < magazine.length(); i++) arr[magazine.charAt(i)- 'a']++;
        for (int i = 0; i < ransomNote.length(); i++) if (--arr[ransomNote.charAt(i)- 'a'] < 0) return false;
        return true;
    }
}