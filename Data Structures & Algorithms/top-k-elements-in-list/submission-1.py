class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        arr = []
        for num, count in d.items():
            arr.append([count, num])

        arr.sort()
        arr.reverse()
        c = 0
        result = []
        while len(result) < k:
            result.append(arr[c][1])
            c+=1
        
        return result