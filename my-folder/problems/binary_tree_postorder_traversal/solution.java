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
    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> l = new LinkedList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        while (!stk.isEmpty()) {
            TreeNode curr = stk.pop();
            if (curr != null) {
                l.addFirst(curr.val);
                stk.push(curr.left);
                stk.push(curr.right);
            }
            
        }
        
        // while (curr != null && !stk.isEmpty()) {
        //     while (curr != null) {
        //         stk.push(curr);
        //         curr = curr.left;
        //     }
        //     curr = stk.pop();
        //     list.add(curr.val);
        //     curr = curr.right;
        // }
    
        return l;
    }
}