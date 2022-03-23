/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean found = false;
    int leafSum = 0;
    public boolean hasPathSum(TreeNode root, int targetSum) {
        hasPathSum(root, targetSum, leafSum);
        return found;
    }
    
    private void hasPathSum(TreeNode root, int targetSum, int leafSum) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            if (targetSum == leafSum + root.val) found = true;
            System.out.println(leafSum);
        }
        hasPathSum(root.left, targetSum, leafSum + root.val);
        hasPathSum(root.right, targetSum, leafSum + root.val);
        
    }
}