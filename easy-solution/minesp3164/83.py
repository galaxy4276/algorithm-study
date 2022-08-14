# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        fast = head.next
        slow = head
        while slow.next:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = slow.next
            else:
                fast, slow = fast.next, slow.next
        return head
