135 Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

思路1：贪心法，先正序遍历数组，如果ratings[i] > ratings[i-1]，num[i] = num[i-1] + 1；再逆序遍历数组，如果ratings[i-1] > ratings[i]，num[i-1] = num[i] + 1
思路2：如果数列递增，则num[i] = num[i-1] + 1；如果数列非递增，设非递增数列的长度为length，非递增数列的首个元素应为num[start] =  max(num[start]+1, length)