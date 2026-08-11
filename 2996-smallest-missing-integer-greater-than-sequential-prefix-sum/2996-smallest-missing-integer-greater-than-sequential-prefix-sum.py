from collections import Counter
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        #My Code :Time: O(n),Space:O(n)
        # s=nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]+1:
        #         s+=nums[i]
        #     else:
        #         break
        # freq=Counter(nums)
        # while True:
        #     if freq[s]==0:
        #         return s
        #     else:
        #         s+=1
        # A bit improved code but with same time & Space Complexity
        sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                sum+=nums[i]
            else:
                break
        s=set(nums)
        while sum in s:
            sum+=1
        return sum
