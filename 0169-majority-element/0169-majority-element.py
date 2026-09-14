class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #GPT Helped
        '''
        mp={}
        for i in nums:
            mp[i]=mp.get(i,0)+1
        return max(mp,key=mp.get)
        '''
        #boyer-moore-majority-vote-algorithm
        candidate=None
        count=0
        #idhi kuda gpt ey ichindhi 
        for i in nums:
            if count==0:
                candidate=i
            if candidate==i:
                count+=1
            else:
                count-=1
        return candidate
