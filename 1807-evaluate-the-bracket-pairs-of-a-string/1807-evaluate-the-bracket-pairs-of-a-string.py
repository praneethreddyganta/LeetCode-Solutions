class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i=0
        knowledge_dict=dict(knowledge)
        ans=""
        #Motham Gpt helped
        while i< len(s):
            if s[i]=="(":
                j=i+1
                while s[j]!=")":
                    j+=1
                ans+=knowledge_dict.get(s[i+1:j],"?")
                i=j
            else:
                ans+=s[i]
            i+=1

        return ans
