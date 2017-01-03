138 Copy List With Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

思路：设原链表是A->B->C->D(假装有random pointer)，先忽略random pointer得到新链表A->A'->B->B'->C->C'->D->D'，然后复制random pointer：pold.next.random = pold.random.next; pold = pold.next.next，最后将old和new分开：pold.next = pnew.next; pold = pold.next; pnew.next = pold.next; pnew = pnew.next