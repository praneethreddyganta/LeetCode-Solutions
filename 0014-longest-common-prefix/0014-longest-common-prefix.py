class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Karthik helped
        min_str=None
        min_len=0
        for str in strs:
            min_len=min(min_len,len(str))
            if min_str==None or len(min_str)>len(str) :
                min_str=str
        ans=''
        for i in range(len(min_str)):
            curr=min_str[i]
            for word in strs:
                if word[i]!=curr:
                    return ans
            ans+=curr
        return ans       
        