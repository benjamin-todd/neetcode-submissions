class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        keys = sorted(count.items(), key = lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(keys[i][0])

        return res