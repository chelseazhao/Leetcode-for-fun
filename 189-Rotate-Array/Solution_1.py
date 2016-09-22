class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        this_to_move = 0
        current = nums[0]
        dis = 0
        for i in range(n):
            next_to_move = (this_to_move + k) % n
            temp = nums[next_to_move]
            nums[next_to_move] = current
            this_to_move = next_to_move
            current = temp
            dis = (dis + k) % n
            if dis == 0:
                this_to_move = (this_to_move + 1) % n
                current = nums[this_to_move]
