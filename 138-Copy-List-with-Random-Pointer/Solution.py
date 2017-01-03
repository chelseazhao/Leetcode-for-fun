# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
        	return
        result = RandomListNode(0)
        pnew = result
        pold = head
        poldNext = None
        flag = True
        while pold:
        	poldNext = pold.next
        	pnew = RandomListNode(pold.label)
        	pold.next = pnew
        	pnew.next = poldNext
        	if flag:
        		result = pnew
        		flag = False
        	pold = poldNext
        pold = head
        while pold:
        	if pold.random:
        		pold.next.random = pold.random.next
        	pold = pold.next.next
        pold = head
        pnew = result
        while pnew.next:
        	pold.next = pnew.next
        	pold = pold.next
        	pnew.next = pold.next
        	pnew = pnew.next
        pnew.next = None
        pold.next = None
        return result