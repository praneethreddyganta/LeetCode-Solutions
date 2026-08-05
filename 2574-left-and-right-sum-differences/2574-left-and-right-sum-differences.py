class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_sum=[]
        right_sum=[0]*n
        l_sum=0
        r_sum=0
        diff=[0]*n
        for i in range(n):
            left_sum.append(l_sum)
            l_sum+=nums[i]
        for j in range(n-1,-1,-1):
            right_sum[j]=r_sum
            r_sum+=nums[j]
        for k in range(n):
            diff[k]=abs(left_sum[k]-right_sum[k])
        return diff


