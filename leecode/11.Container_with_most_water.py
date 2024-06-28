class Solution:
    def maxArea(self, height) -> int:
        left_point = 0
        right_point = len(height)-1
        max_water = 0

        while left_point <= right_point:
            Min_height = min(height[left_point], height[right_point])
            max_water = max(Min_height*(right_point-left_point), max_water)
            if height[left_point] > height[right_point]:
                right_point -= 1
            else:
                left_point += 1
        print(max_water)
        return max_water

test = Solution()
test.maxArea([1,1])