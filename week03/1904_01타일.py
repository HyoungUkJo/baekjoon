""" 
1이라는 타일과 00이라는 타일이 있는데 이걸로 수를 만들어야함.
N=1일때 한가지의 경우밖에는 없을듯

어떤 규칙으로 증가를 하는지 알아봐야함.

"""
def tile(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    return dp[n]

N = int(input())

print(tile(N))

