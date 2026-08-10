class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val=nums[0]
        for i in range(1,len(nums)):
            if abs(nums[i])<abs(val):
                val=nums[i]
            elif abs(nums[i])==abs(val):
                val=max(nums[i],val)
        return val


        