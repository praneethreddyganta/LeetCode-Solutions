class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min=[0]*len(nums)
        max=[0]*len(nums)
        min[-1]=nums[-1]
        max[0]=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>max[i-1]:
                max[i]=nums[i]
            else:
                max[i]=max[i-1]
        for j in range(len(nums)-2,-1,-1):
            if nums[j]<min[j+1]:
                min[j]=nums[j]
            else:
                min[j]=min[j+1]
                
        for m in range(len(nums)):
            if max[m]-min[m]<=k:
                return m
        return -1      