class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i=0
        knowledge_dict=dict(knowledge)
        ans=""
        while i< len(s):
            if s[i]=="(":
                j=i+1
                while j<len(s):
                    if s[j]==")":
                        t=i
                        i=j
                    
                        break
                        
                    j+=1
                ans+=knowledge_dict.get(s[t+1:j],"?")
            else:
                ans+=s[i]
            i+=1

        return ans
