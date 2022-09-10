public class Solution {
    public boolean hasCycle(ListNode head) {
        ArrayList<ListNode> arraylist = new ArrayList();
        if (head == null){
            return false;
        }
        if (head.next == null){
            return false;
        }
        
        while(true){
            arraylist.add(head);
            head = head.next;
            
            for(int i  = 0 ; i < arraylist.size() ; i++){
                if (arraylist.get(i) == head){
                    return true;
                }
            }
            
            if (head.next == null){
                break;
            }
        }
        return false;
        
    }
}
//실패 코드 
/**
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<Integer> set = new HashSet<>();
        boolean result = false;
        while(head!=null){
            if(head.next==null) {
                result = false;
                break;
            }
            else {
                if(set.contains(head.val)) {
                    result = true;
                    break;
                }
                set.add(head.val);
                head=head.next;
            }
        }
        return result;
    }
}
**/
