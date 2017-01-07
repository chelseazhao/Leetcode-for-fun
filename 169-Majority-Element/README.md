169 Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

思路：Moore’s voting algorithm：每次都找出一对不同的元素，从数组中删掉，直到数组为空或只有一种元素。 不难证明，如果存在元素e出现频率超过半数，那么数组中最后剩下的就只有e。当然，最后剩下的元素也可能并没有出现半数以上。比如说数组是[1, 2, 3]，最后剩下的3显然只出现了1次，并不到半数。排除这种false positive 情况的方法也很简单，只要保存下原始数组，最后扫描一遍验证一下就可以了。
在算法执行过程中，我们使用常量空间实时记录一个候选元素c以及其出现次数f(c)， c即为当前阶段出现次数超过半数的元素。
在遍历开始之前，该元素c为空，f(c)=0。
然后在遍历数组A时，如果f(c)为0，表示当前并没有候选元素，也就是说之前的遍历过程中并没有找到超过半数的元素。那么，如果超过半数的元素c存在，那么c在剩下的子数组中，出现次数也一定超过半数。因此我们可以将原始问题转化为它的子问题。此时c赋值为当前元素, 同时f(c)=1。
如果当前元素A[i] == c, 那么f(c) += 1。(没有找到不同元素，只需要把相同元素累计起来)
如果当前元素A[i] != c，那么f(c) -= 1。 (相当于删除1个c)，不对A[i]做任何处理(相当于删除A[i])
如果遍历结束之后，f(c)不为0，那么元素c即为寻找的元素。上述算法的时间复杂度为O(n)， 而由于并不需要真的删除数组元素，我们也并不需要额外的空间来保存原始数组，空间复杂度为O(1)。