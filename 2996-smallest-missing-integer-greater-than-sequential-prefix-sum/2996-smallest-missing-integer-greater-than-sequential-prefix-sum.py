from collections import Counter
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                s+=nums[i]
            else:
                break
        freq=Counter(nums)
        while True:
            if freq[s]==0:
                return s
            else:
                s+=1