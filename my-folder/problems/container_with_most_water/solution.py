class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        most_water = 0
        while l < r:
            width = r - l
            h = 0
            if height[l] < height[r]:
                h = l
                l += 1
            else:
                h = r
                r -= 1
            most_water = max(width * height[h], most_water)
        return most_water
            