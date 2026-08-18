from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq=Counter(nums)
        n=len(nums)
        #Leetcode lo hints chusina
        if k==1:
            ans=-1
            for num,count in freq.items():
                if count==1:
                    ans=max(ans,num)
            return ans
        elif k==n:
            return max(nums)
        else:
            ans=-1
            if freq[nums[0]]==1:
                ans=nums[0]
            if freq[nums[-1]]==1:
                ans=max(ans,nums[-1])
            return ans

