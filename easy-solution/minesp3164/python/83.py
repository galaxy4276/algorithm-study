# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        fast = head.next
        slow = head
        while fast.next:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = slow.next
            else:
                fast, slow = fast.next, slow.next
        return head
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list =  ListNode(0)
        sumlist = list
        while list1 and list2 :
            if list1.val <= list2.val:
                sumlist.next = list1
                list1 = list1.next
            else :
                sumlist.next = list2
                list2 = list2.next
            sumlist = sumlist.next
        sumlist.next = list1 or list2

        return sumlist.next
"""