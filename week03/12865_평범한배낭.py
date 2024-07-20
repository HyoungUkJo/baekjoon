N, K = map(int,input().split())

# 물건의 무개와 가중치를 2차원 배열로 받아서 이후에 값을 비교한다.
knap = [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]
for _ in range(N):
    knap.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        #무개와 가중치 값 할당
        weight = knap[i][0]
        value  = knap[i][1]
        # j가 무개보다 더 작다면 값이 들어갈 수 없음으로 이전 배열의 가중치를 가지고 온다.
        if j<weight :
            dp[i][j] = dp[i-1][j]
        # 가중치가 무개보다 더 크다면 이전값과 새로 계산한 값의 가중치를 비교해서 더 높은 가격으로 들어가게 된다.
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[N][K])
    