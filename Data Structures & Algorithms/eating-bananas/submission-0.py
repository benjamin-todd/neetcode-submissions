class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = sum(math.ceil(p / k) for p in piles)
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res