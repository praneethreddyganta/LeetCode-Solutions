class Solution:
    import math
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq={}
        window_sum=0
        max_sum=0
        for i in range(k):
            freq[nums[i]]=freq.get(nums[i],0)+1
            window_sum+=nums[i]
        if len(freq)==k:
            max_sum=window_sum
        for j in range(k,n):
            incoming=nums[j]
            outgoing=nums[j-k]
            window_sum+=nums[j]
            freq[incoming]=freq.get(incoming,0)+1
            window_sum-=nums[j-k]
            freq[outgoing]-=1
            if freq[outgoing]==0:
                del freq[outgoing]
            if len(freq)==k:
                max_sum=max(max_sum,window_sum)

        return max_sum
        