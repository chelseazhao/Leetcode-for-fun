# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return
        # split
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        # reverse the second list
        newHead = ListNode(0)
        newHead.next = head2
        point = head2.next
        head2.next = None
        while point:
            tmp = point
            point = point.next
            tmp.next = newHead.next
            newHead.next = tmp
        head2 = newHead.next
        # merge
        p1 = head1
        p2 = head2
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 =tmp1
            p2 =tmp2
