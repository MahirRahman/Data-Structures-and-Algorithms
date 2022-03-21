/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode[] temp = new ListNode[100];
        int size = 0;
        while (head != null) {
            temp[size++] = head; 
            head = head.next;
        }
        int mid = (int) Math.floor(size / 2.0);
        return temp[mid];
        // String ret = "";
        // for (int i = mid; i < size; i++) ret += ", " + temp.val;
        // return "[ " + ret.substring(2) + "]";
    }
}