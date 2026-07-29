from collections import Counter
from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def count_ways(chars):
            #Motham GPT ey help chesindhi ina sagam sagamey ardham indhi .Problem of the day kosam cheyalsi ochindhi 
            total=sum(chars.values())
            res=1
            rem=total
            for ch in sorted(chars):
                c=half[ch]
                if c:
                    res*=comb(rem,c)
                    if res>k:
                        return k+1
                    rem-=c
            return res

        freq=Counter(s)
        half={}
        middle=""
        for ch,cnt in freq.items():
            half[ch]=cnt//2
            if cnt%2==1:
                middle=ch
        chars=sorted(half)
        if count_ways(half)<k:
            return ""
        left_len=len(s)//2
        left=[]
        for i in range(left_len):
            for ch in chars:
                if half[ch]==0:
                    continue
                half[ch]-=1

                count=count_ways(half)
                if count>=k:
                    left.append(ch)
                    break
                else:
                    k-=count
                    half[ch]+=1
        left_str="".join(left)
        return left_str+middle+left_str[::-1]

        