class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod=[1]*(len(nums))
        suffix_prod=[1]*(len(nums))
        prod=[1]*len(nums)
        prefix=1
        suffix=1
        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            prefix_prod[i]=prefix
        for i in range(len(nums)-2,-1,-1):
            suffix*=nums[i+1]
            suffix_prod[i]=suffix
            prod[i]=prefix_prod[i]*suffix_prod[i]
        prod[len(nums)-1]=prefix_prod[len(nums)-1]*suffix_prod[len(nums)-1]
        return prod
        