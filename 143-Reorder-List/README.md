143 Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}. 

思路：用快慢指针把列表分割为两部分，将第二个列表翻转，再将第一个列表和翻转后的第二个列表连接在一起。