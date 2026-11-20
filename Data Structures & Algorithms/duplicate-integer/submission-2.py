class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = dict()

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for key, num in count.items():
            if num >= 2:
                return True
        
        return False