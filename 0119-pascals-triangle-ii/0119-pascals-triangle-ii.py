class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #Took GPT ans Striver's Help
        triangle=[0]*(rowIndex+1)
        triangle[0]=1
        for i in range(1,rowIndex+1):
            triangle[i]=(triangle[i-1]*(rowIndex+1-i))//i
        return triangle

            