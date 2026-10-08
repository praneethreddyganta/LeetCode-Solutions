class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #Took GPT ans Striver's Help
        triangle=[[1]]
        for i in range(1,rowIndex+1):
            prev=triangle[-1]
            curr=[1]
            for j in range(1,len(prev)):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            triangle.append(curr)
        return triangle[rowIndex]