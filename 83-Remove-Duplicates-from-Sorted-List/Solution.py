# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        h = head
        while h is not None and h.next is not None:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next
        return head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    print sol.deleteDuplicates(head)
        
