# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        array = []
        answer = 0
        a = 0
        while head:
            array.append(head.val)
            head = head.next
        for i in range(len(array)-1, -1 , -1):
            answer += array[i] * (2**a)
            a+= 1
        return answer

## solution
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num