class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for (int i = 0; i < accounts[0].length; i++) {
            max += accounts[0][i];
        }
        for (int i = 1; i < accounts.length; i++) {
            int total  = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                total += accounts[i][j];
            }
            if (total > max) max = total;
        }
            return max;
    }

}