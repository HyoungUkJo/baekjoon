def padoban(n):
    # dp=[0]*(n+2)
    # dp[1]=1
    # dp[2]=1
    # dp[3]=1
    # dp[4]=2
    # if n <= 3:
    #     return dp[n]
    # for i in range(4,n+1):
    #     dp[i]=dp[i-1]+dp[i-5]
    if n <= 5:
        return [1, 1, 1, 2, 2][n-1]    
    dp=[0]*n
    dp[0]=1
    dp[1]=1
    dp[2]=1
    dp[3]=2
    dp[4]=2
    dp[5]=3
    for i in range(5,n):
        dp[i]=dp[i-1]+dp[i-5]
    return dp[n-1]
T = int(input())

for _ in range(T):
    N = int(input())

    print(padoban(N))
# 4%에서 runtime error