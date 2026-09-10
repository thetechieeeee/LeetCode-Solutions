class Solution:
    def spiralOrder(self,mat):
        ans=[]
        t=0
        b=len(mat)-1
        l=0
        r=len(mat[0])-1
        while t<=b and l<=r:
            for i in range(l,r+1):
                ans.append(mat[t][i])
            t+=1
            for i in range(t,b+1):
                ans.append(mat[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    ans.append(mat[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    ans.append(mat[i][l])
                l+=1
        return ans
s=Solution()
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(s.spiralOrder(matrix))