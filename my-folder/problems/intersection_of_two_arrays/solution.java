class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> hs = new HashSet<>();
        Set<Integer> hs1 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            hs.add(nums1[i]);
        }
        int[] nums = new int[hs.size()];
        int index = 0;
        for (int i = 0; i < nums2.length; i++) {
            if (hs.contains(nums2[i])) {
                if (hs1.add(nums2[i])) {
                    nums[index++] = nums2[i];
                }
            }
        }
        return Arrays.copyOf(nums, index);
    }
}