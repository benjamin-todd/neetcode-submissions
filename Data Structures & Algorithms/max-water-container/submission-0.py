class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        res = 0
        while l < r:
            diff = r - l
            prod = min(heights[l],heights[r]) * diff
            res = max(prod, res)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return res
