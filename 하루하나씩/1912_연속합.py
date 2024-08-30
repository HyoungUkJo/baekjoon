def con_add(N,arr):
    dp = [0]*(N+1)
    for i in range(1,N+1):
        dp[i] = max(dp[i-1]+arr[i-1],arr[i-1])
        # print(dp)
    return max(dp[1:N+1])
N = int(input())

arr= list(map(int, input().split()))

print(con_add(N,arr))
 