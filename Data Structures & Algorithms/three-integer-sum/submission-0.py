class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                if nums[i]+nums[left]+nums[right]==0:
                    arr = []
                    arr.append(nums[i])
                    arr.append(nums[left])
                    arr.append(nums[right])
                    res.append(arr)
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left+=1
                else:
                    right-=1

        return res