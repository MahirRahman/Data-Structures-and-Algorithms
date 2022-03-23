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
    // public List<Integer> inorderTraversal(TreeNode root) {
    //     List<Integer> list = new LinkedList<Integer>();
    //     Stack<TreeNode> stack = new Stack<TreeNode>();
    //     stack.push(root);
    //     while (!stack.isEmpty()) {
    //         TreeNode visiting = stack.pop();
    //         if (visiting != null) {
    //             stack.push(visiting.right);
    //             stack.push(visiting.left);
    //             list.add(visiting.val);
    //         }
    //     }
    //     return list;
    // }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new LinkedList<Integer>();
        inorderTraversal(root, list);
        return list;
    }
    
    public void inorderTraversal(TreeNode root, List<Integer> list) {
        if (root == null) return;
        if (root.left != null) inorderTraversal(root.left, list);
        list.add(root.val);
        if (root.right != null) inorderTraversal(root.right, list);   
    }
}