# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def doReverse(self, head, num):
        pre = ListNode(0)
        pre.next = head
        pointer = head
        for i in range(0, num):
            tmp = head
            head = head.next
            tmp.next = pre
            pre = tmp
        pointer.next = head
        return pre

    
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        preHead = ListNode(0)
        result = preHead
        preHead.next = head
        for i in range(0, m - 1):
            preHead = preHead.next
        preHead.next = self.doReverse(preHead.next, n-m+1)
        return result.next
