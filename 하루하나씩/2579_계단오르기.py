N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0] * (N+1)

dp[0]=arr[0]
dp[1]=max(arr[0]+arr[1],arr[1])
# for i in range(2,N):
    # dp[i]=max(arr[])