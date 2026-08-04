class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        small=float('inf')
        large=float('-inf')
        for i in range(n):
            if nums[i]< small:
                small=nums[i]
            if nums[i]>large:
                large=nums[i]
        ele=small+1
        l=[]
        while ele<large:
            if ele not in nums:
                l.append(ele)
            ele+=1
        return l

            
        