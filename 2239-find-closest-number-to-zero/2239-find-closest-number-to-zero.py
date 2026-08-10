class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val=float('inf')
        for i in range(len(nums)):
            if abs(nums[i]-0)<abs(val-0):
                val=nums[i]
            elif abs(nums[i]-0)==abs(val-0):
                val=max(nums[i],val)
        return val


        