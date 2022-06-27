# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        x = r = ListNode(0)
        while l1 != None or l2 != None or c != 0:
            v = 0
            if l1:
                v += l1.val
                l1 = l1.next
            if l2: 
                v += l2.val
                l2 = l2.next
            
            v += c
            c = v / 10 
            
            r.next = ListNode(v % 10)
            r = r.next
        return x.next
               