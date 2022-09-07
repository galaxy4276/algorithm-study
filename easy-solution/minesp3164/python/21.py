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