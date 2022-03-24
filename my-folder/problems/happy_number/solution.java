class Solution {
    public boolean isHappy(int n) {
        Set<Integer> sh = new HashSet<>();
        int sum = 0;
        int holder = 0;
        while (sum != 1) {
            sum = 0;
            while (n > 0) {
                sum += Math.pow(n % 10, 2.0);
                n = n / 10;
            }
            if (!sh.add(sum)) return false;
            n = sum;
        }
        return true;
    }
}