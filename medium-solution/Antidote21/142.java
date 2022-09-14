public class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> set = new HashSet<ListNode>();
      
        while(head!=null){
            if(!set.add(head)){
                return head;
            }
            head = head.next;
        }
      
        return null;
        
    }
}

