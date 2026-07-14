class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''n=len(nums)
        left_arr=[0]
        prefix_sum=0
        for i in range(1,n):
            prefix_sum+=nums[i-1]
            left_arr.append(prefix_sum)
        right_arr=[0]*n
        suffix_sum=0
        for j in range(n-1,-1,-1):
            right_arr[j]=suffix_sum
            suffix_sum+=nums[j]
        for i in range(n):
            if left_arr[i]==right_arr[i]:
                return i
        return -1
'''
        #GPT Given Time:O(N),Space:O(1)
        n=len(nums)
        total_sum=sum(nums)
        left_sum=0
        for i in range(n):
            right_sum=total_sum-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1


        
            
