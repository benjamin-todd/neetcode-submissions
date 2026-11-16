class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            best = max(best, (r - l) * min(heights[r],heights[l]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return best