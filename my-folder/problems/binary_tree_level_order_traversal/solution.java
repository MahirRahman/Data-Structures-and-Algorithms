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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> finalList = new LinkedList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> l = new LinkedList<Integer>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.remove();
                if (curr != null) {
                l.add(curr.val);
                q.add(curr.left);
                q.add(curr.right);
            }
            }
            if (l.size() != 0)
            finalList.add(l);
        }
        
        return finalList;
        
    }
}