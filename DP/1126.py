import sys

N=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))
sm=sum(num)
dp=[[0]*(sm+1) for _ in range(N)]
for i in range(1, sm+1):
    dp[0][i]=-1
dp[0][num[0]]=num[0]
for i in range(1, N):
    for j in range(sm+1):
        dp[i][j]=dp[i-1][j]
        if num[i]+j<sm+1 and dp[i-1][num[i]+j]!=-1:
            dp[i][j]=max(dp[i][j], dp[i-1][num[i]+j])
        if num[i]<=j and dp[i-1][j-num[i]]!=-1:
            dp[i][j]=max(dp[i][j], dp[i-1][j-num[i]]+num[i])
        if num[i]>j and dp[i-1][num[i]-j]!=-1:
            dp[i][j]=max(dp[i][j], dp[i-1][num[i]-j]+j)
if dp[N-1][0]<=0:
    print(-1)
else:
    print(dp[N-1][0])
