class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=float('-inf')
        prefix_product=1
        suffix_product=1
        for i in range(len(nums)):          
            prefix_product*=nums[i]
            suffix_product*=nums[len(nums)-1-i]
            max_product=max(max_product,prefix_product,suffix_product)
            if prefix_product==0:
                prefix_product=1
            if suffix_product==0:
                suffix_product=1  
        return max_product
