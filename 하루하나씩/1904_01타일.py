def tile(n):
    dp=[0]*(n+2)
    dp[1]=1
    dp[2]=2
    if n <= 2:
        return dp[n]
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    return dp[n]
N = int(input())
# N = N%15746
print(tile(N))