class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> hs = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!hs.add(nums[i])) {
                hs.remove(nums[i]);
            }
        }
        // for (int i = 0; i < nums.length; i++) {
        //     if (hs.contains(nums[i])) return nums[i];
        // }
        return (int)hs.toArray()[0];
    }
}