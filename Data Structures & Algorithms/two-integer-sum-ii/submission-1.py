class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = None
        l = 0
        r = len(numbers) - 1
        while res != target:
            res = numbers[l] + numbers[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
        return [l+1,r+1]