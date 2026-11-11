class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            diff = r - l
            height = min(heights[r], heights[l])
            prod = height * diff
            res = max(prod, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res