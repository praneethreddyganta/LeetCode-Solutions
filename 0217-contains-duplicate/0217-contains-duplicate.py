class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # freq={}
        # for ch in nums:
        #     freq[ch]=freq.get(ch,0)+1
        # if max(freq.values())>=2:
        #     return True
        # else:
        #     return False
        #Optimal code I have seen in one of the submission-submit chesina valla code chusina
        s=set(nums)
        if len(nums)==len(s):
            return False
        else:
            return True
        