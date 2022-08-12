# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_step = head
        half_step = head
        
        middle_node = None
        
        def node_validator(node) :
            if node == None :
                return True
            
            else :
                return False
        
        while True :
            fast_step = fast_step.next
            
            is_last_node = node_validator(fast_step)
                        
            if is_last_node :
                return half_step
            
            fast_step = fast_step.next
            
            half_step = half_step.next
            
            is_last_node = node_validator(fast_step)
            
            if is_last_node :
                return half_step