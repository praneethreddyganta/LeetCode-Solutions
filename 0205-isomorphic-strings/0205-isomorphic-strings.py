class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #GPT Helped nenu 1 hashmap vadi try chesina but pakkaga 2 vadalu adhi nenu chesina mistake and strivers approach antha sarigga ardham kaley....
        # E problem malli chusthey pakka strivers approach try chey 
        s_map={}
        t_map={}
        for i in range(len(s)):
            if s[i] in s_map and t[i]!=s_map[s[i]]:
                return False
            if t[i] in t_map and s[i]!=t_map[t[i]]:
                return False
            s_map[s[i]]=t[i]
            t_map[t[i]]=s[i]
        return True