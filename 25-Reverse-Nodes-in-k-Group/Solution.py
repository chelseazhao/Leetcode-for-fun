# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, head, end):
        new_head = ListNode(0)
        new_head.next = head
        while new_head.next != end:
            temp = head.next
            head.next = temp.next
            temp.next = new_head.next
            new_head.next = temp
        return [end, head]
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if k == 0 or k == 1:
            return head
        new_head = ListNode(0)
        new_head.next = head
        start = new_head
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if end.next == None:
                    return new_head.next
            result = self.reverse(start.next, end.next)
            start.next = result[0]
            start = result[1]
        return new_head.next
                    
