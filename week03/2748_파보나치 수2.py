def fibo_memo(n, memo=None):
    if memo is None:
        memo={}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n]=fibo_memo(n-1,memo)+fibo_memo(n-2,memo)

    return memo[n]

def fibo_table(n):
    if n<=1:
        return n
    
    dp = [0]*(n+1)
    dp[0]=1
    dp[1]=1

    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]
    



N = int(input())

# print(fibo_memo(N))
print(fibo_table(N))

