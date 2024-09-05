N = int(input())
dp = []
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    dp.append([0] * (i + 1))

for i in range(N):
    for j in range(len(arr[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]
        elif j == len(arr[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]

print(max(dp[N-1]))