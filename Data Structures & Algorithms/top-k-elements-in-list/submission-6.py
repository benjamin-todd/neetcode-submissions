class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
           res.append(sorted_count[i][0]) 

        return res