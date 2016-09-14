class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        max_area = 0
        while left < right:
            this_height = height[left] if height[left] < height[right] else height[right]
            area = this_height * (right - left)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area
if __name__ == "__main__":
    height = [1, 2]
    solution = Solution()
    print solution.maxArea(height)
                
