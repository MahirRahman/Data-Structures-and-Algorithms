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
    public TreeNode searchBST(TreeNode root, int val) {
        //  if (root == null) return null;
        // if (root.val == val) return root;
        // else if (root.val > val) return searchBST(root.left, val);
        // else return searchBST(root.right, val);       
        Stack<TreeNode> stk = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stk.isEmpty()) {
            while (curr != null) {
                stk.push(curr);
                curr = curr.left;
            }
            curr = stk.pop();
            if (curr.val == val) return curr;
            curr = curr.right;
        }
        return null;
        
        
    }
}