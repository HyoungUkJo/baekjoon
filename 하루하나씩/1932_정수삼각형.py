N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

dp[0]=arr[0]
for i in range(1,N):
    for j in range(i):
        if j==0:
            dp[i][j]=dp[i-1][j]+arr[i][j]
        else :
            dp[i][j]=dp[i-1][j]+max(arr[i][j],arr[i][j+1])
        

print(dp)
print(max(dp[N-1]))