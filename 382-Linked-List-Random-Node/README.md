382 Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

思路：蓄水池算法(reservoir sampling)
在序列流中取一个数，如何确保随机性，即取出某个数据的概率为:1/(已读取数据个数)
　　假设已经读取n个数，现在保留的数是Ax，取到Ax的概率为(1/n)。
　　对于第n+1个数An+1，以1/(n+1)的概率取An+1，否则仍然取Ax。依次类推，可以保证取到数据的随机性。
　　数学归纳法证明如下：
　　　　当n=1时，显然，取A1。取A1的概率为1/1。
           假设当n=k时，取到的数据Ax。取Ax的概率为1/k。
           当n=k+1时，以1/(k+1)的概率取An+1，否则仍然取Ax。
　　　　(1)如果取Ak+1，则概率为1/(k+1)；
　　　　(2)如果仍然取Ax，则概率为(1/k)*(k/(k+1))=1/(k+1)
所以，对于之后的第n+1个数An+1，以1/(n+1)的概率取An+1，否则仍然取Ax。依次类推，可以保证取到数据的随机性。

在序列流中取k个数，如何确保随机性，即取出某个数据的概率为:k/(已读取数据个数)
　　建立一个数组，将序列流里的前k个数，保存在数组中。(也就是所谓的"蓄水池")
　　对于第n个数An，以k/n的概率取An并以1/k的概率随机替换“蓄水池”中的某个元素；否则“蓄水池”数组不变。依次类推，可以保证取到数据的随机性。
　　数学归纳法证明如下：
　　　　当n=k是，显然“蓄水池”中任何一个数都满足，保留这个数的概率为k/k。
           假设当n=m(m>k)时，“蓄水池”中任何一个数都满足，保留这个数的概率为k/m。
           当n=m+1时，以k/(m+1)的概率取An，并以1/k的概率，随机替换“蓄水池”中的某个元素，否则“蓄水池”数组不变。则数组中保留下来的数的概率为：
所以，对于第n个数An，以k/n的概率取An并以1/k 的概率随机替换“蓄水池”中的某个元素；否则“蓄水池”数组不变。依次类推，可以保证取到数据的随机性。