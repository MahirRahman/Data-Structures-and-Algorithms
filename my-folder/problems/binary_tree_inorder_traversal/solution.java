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
//     public List<Integer> inorderTraversal(TreeNode root) {
//         List<Integer> list = new LinkedList<Integer>();
//         inorderTraversal(root, list);
//         return list;
//     }
    
//     public void inorderTraversal(TreeNode root, List<Integer> list) {
//         if (root == null) return;
//         if (root.left != null) inorderTraversal(root.left, list);
//         list.add(root.val);
//         if (root.right != null) inorderTraversal(root.right, list);   
//     }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        Deque<TreeNode> stk = new LinkedList<>();
        List<Integer> lst = new LinkedList<>();
        TreeNode curr = root;
        while (curr != null || !stk.isEmpty()) {
            while (curr != null) {
                stk.push(curr);
                curr = curr.left;
            }
            curr = stk.poll();
            lst.add(curr.val);
            curr = curr.right;    
        }
        return lst;
    }
}