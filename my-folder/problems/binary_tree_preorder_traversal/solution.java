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
//     public List<Integer> preorderTraversal(TreeNode root) {
//         List<Integer> l = new ArrayList<Integer>();
//         preorderTraversal(root, l);
//         return l;
//     }
    
//     public void preorderTraversal(TreeNode root, List<Integer> l) {
//         if (root == null) return;
//         l.add(root.val);
//         if (root.left != null) preorderTraversal(root.left, l);
//         if (root.right != null) preorderTraversal(root.right, l);
//     }
    
     public List<Integer> preorderTraversal(TreeNode root) {
         List<Integer> list = new LinkedList<Integer>();
         // if (root == null) return list;
         Stack<TreeNode> tovisit = new Stack<TreeNode>();
         tovisit.push(root);
         while (!tovisit.isEmpty()) {
             TreeNode visiting = tovisit.pop();
             if (visiting != null) {
             list.add(visiting.val);
                 tovisit.push(visiting.right);
            tovisit.push(visiting.left);
             }
         }
         
         return list;
         
     }
    
}