# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        answer = None
        while head:
            temp = head
            head = head.next
            temp.next = answer
            answer = temp
        return answer
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head   #Empty.
        if not head.next: return head   #We reached end.
        orig_head = self.reverseList(head.next)  #Traverse to end, orig_head is now end node.
        head.next.next = head   #Swap head with right node.
        head.next = None   #So we don't wind up in infinite loop.
        return orig_head   #Very last thing returned. End node!
        """



