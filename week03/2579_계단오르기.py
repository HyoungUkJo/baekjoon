N = int(input())

arr = []

for _ in range(N):
    a = int(input())
    arr.append(a)

# dp = [[0]*(N+1) for _ in range(N+1)]
dp = [0]*(N)
# 10 20 15 25 10 20
# 값을 미리 정해놓고 이를 비교하면서 쌓을 수 있게..
# 큰 인덱스랑 비교해버리면 인덱스 초과 날듯
dp[0] = arr[0]
dp[1] = arr[1]+arr[0]
dp[2] = max(dp[0]+arr[2],dp[0]+arr[1])
for i in range(3,N):
    dp[i] = max(arr[i]+arr[i-1]+dp[i-3],dp[i-2],arr[i])
#     print(f'dp[{i-1}]+arr[{i}]={dp[i-1]+arr[i]},dp[{i-1}]+arr[{i-1}={dp[i-1]+arr[i-1]}]')
#     dp[i]=max(dp[i-1]+arr[i],dp[i-1]+arr[i-1])

    # for j in range(1,N+1):
    #     if dp[i][j] < arr[j]:
print(dp[N-1])