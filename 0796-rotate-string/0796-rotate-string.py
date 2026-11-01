class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #Nadhi kanisam brute force kua kadhu .INkamanchiga improve cheyali
        s1=list(s)
        for i in range(len(s1)):
            temp=s1[0]
            for j in range(len(s1)-1):
                s1[j]=s1[j+1]
            s1[-1]=temp
            if "".join(s1)==goal:
                return True
        return False
        