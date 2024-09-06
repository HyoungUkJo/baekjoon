N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0]*(N+1)
dp[0]=0
dp[1]=dp[0]+arr[1]
dp[2]=dp[1]+arr[2]
dp[3] = max(dp[1]+arr[3],dp[0]+arr[3])

for i in range(4,N):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[N-1])
