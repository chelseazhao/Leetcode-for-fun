61 Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

思路：先遍历链表得到长度，然后重新遍历，两个相邻指针。