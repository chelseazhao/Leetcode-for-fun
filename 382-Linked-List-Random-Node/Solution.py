# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.linkedlist = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result = self.linkedlist
        node = self.linkedlist.next
        index = 1
        while node:
            if random.random() < 1./(index + 1):
                result = node
            node = node.next
            index += 1
        return result.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
