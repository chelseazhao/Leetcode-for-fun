123 Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

思路：用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。最多交易两次，手上最多只能持有一支股票，求最大收益。
动态规划法。以第i天为分界线，先计算第i天之前进行一次交易的最大收益preMax[i]，再逆向扫描，计算第i天之后进行一次交易的最小损失postMin[i]，max{preMax[i] - postMin[i]} (0≤i≤n-1)就是最大收益。第i天之前和第i天之后进行一次的最大收益求法: 动态规划法。从前向后遍历数组，记录当前出现过的最低价格，作为买入价格，并计算以当天价格出售的收益，作为可能的最大收益，整个遍历过程中，出现过的最大收益就是所求。