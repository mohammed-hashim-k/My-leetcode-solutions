class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False
        l1,l2,l3=len(s1),len(s2),len(s3)
        dp=[[-1]*(l2+1)]*(l1+1)
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0 and j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=dp[i][j-1] and s2[j-1]==s3[i+j-1]
                elif j==0:
                    dp[i][j]=dp[i-1][j] and s1[i-1]==s3[i+j-1]
                else:
                    dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[l1][l2]           
        