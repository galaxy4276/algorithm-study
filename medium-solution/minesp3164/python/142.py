# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None

        fast = head
        slow = head
        isCycle = False

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

            if(fast == slow):
                isCycle = True
                break

        if not isCycle:
            return None
        slow = head
        while fast != slow :
            slow = slow.next
            fast = fast.next
        return fast