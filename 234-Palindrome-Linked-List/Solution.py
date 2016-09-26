# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        front = behind = head
        new_list = []
        while behind and behind.next:
            new_list.insert(0, front.val)
            front = front.next
            behind = behind.next.next
        
        if behind != None:
            front = front.next
        for i in range(len(new_list)):
            if front.val != new_list[i]:
                return False
            else:
                front = front.next
        return True
