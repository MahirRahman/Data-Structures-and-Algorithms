class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (words.length != pattern.length()) {
            return false;
        }
        Set<String> wordSet = new HashSet<>();
        Set<Character> patternSet = new HashSet<>();
        for (String word: words) {
            wordSet.add(word);   
        }
        for (int i = 0; i < pattern.length(); i++) {
            patternSet.add(pattern.charAt(i));   
        }
        if (patternSet.size() != wordSet.size()) {
            return false;
        }
        HashMap<String,Character> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            if (!map.containsKey(words[i])) {
                map.put(words[i],pattern.charAt(i));
            }
            else if (map.get(words[i]) != pattern.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}