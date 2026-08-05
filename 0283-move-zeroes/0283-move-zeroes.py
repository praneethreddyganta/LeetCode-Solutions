class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l=0
        # r=1
        # while l<len(nums) and r<len(nums):
        #     if nums[l]==0 and nums[r]!=0:
        #         nums[l],nums[r]=nums[r],nums[l]
        #         l+=1
        #         r+=1
        #     elif nums[l]!=0:
        #         l+=1
        #         r+=1
        #     else:
        #         r+=1
        # return nums
        # better approach :Took TUF Help
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1       