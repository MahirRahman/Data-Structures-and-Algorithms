class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
          ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0; i < mat.length; i++) {
            int total = 0;
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 0 ) break;
                total += mat[i][j];
            }
            arr.add(total);
        }
        
System.out.println(arr);
        int[] sorted = new int[arr.size()];
        int index = 0;
        for (int j = 0; j < arr.size(); j++) {
            int min = 101;
            int weakRow = 0;
            for (int i = 0; i < arr.size(); i++) {
                if (arr.get(i) < min) {
                    min = arr.get(i);
                    weakRow = i;
                }
            }
            System.out.println(arr);
            sorted[index++] = weakRow;
            arr.set(weakRow, 101);
        }
        
        return Arrays.copyOf(sorted, k);
    }
}