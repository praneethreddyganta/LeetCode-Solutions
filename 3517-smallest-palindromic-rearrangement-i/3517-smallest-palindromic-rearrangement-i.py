class Solution:
    def smallestPalindrome(self, s: str) -> str:
        #Total GPT Help and leetcode hints
        freq={}
        for chr in s:
            if chr in freq:
                freq[chr]+=1
            else:
                freq[chr]=1
        chrs=sorted(freq)
        first=""
        for chr in chrs:
            first+=chr*(freq[chr]//2)
        middle=""
        for chr in chrs:
            if freq[chr]%2==1:
                middle=chr
        last=first[::-1]
        ans=first+middle+last
        return ans

