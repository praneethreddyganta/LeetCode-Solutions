class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1=sorted(nums)
        i=0
        j=len(nums1)-1
        l=[]
        while i<j:
            if nums1[i]+nums1[j]==target:
                small=nums1[i]
                big=nums1[j]
                break
            elif nums1[i]+nums1[j]<target:
                i+=1
            else:
                j-=1
        for i in range(len(nums)):
            if nums[i]==small:
                l.append(i)
            elif nums[i]==big:
                l.append(i)
        return l
