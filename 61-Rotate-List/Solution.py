# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        hh = head
        num = 0
        while hh:
            num += 1
            hh = hh.next
        if k >= num:
            k %= num
        if k == 0:
            return head
        h = head
        pointer = head.next
        for i in range(num - k - 1):
            h = h.next
            pointer = pointer.next
        h.next = None
        newHead = pointer
        while pointer.next:
            pointer = pointer.next
        pointer.next = head
        return newHead
