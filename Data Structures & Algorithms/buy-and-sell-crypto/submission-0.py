class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j <= i:
                    continue    
                s = prices[j] - prices[i]
                if s > max:
                    max = s
        if max < 0:
            return 0
        return max

