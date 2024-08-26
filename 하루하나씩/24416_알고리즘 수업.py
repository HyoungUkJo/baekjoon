import sys

code1=0
code2=0

def recursion(n):
    global code1
    if n==1 or n==2:
        code1+=1
        return 1    #코드1
    return recursion(n-1) + recursion(n-2)

def fibo(n):
    global code2
    fibo_dp = [0]*(n+1)
    fibo_dp[0] = 1
    fibo_dp[1] = 1
    fibo_dp[2] = 1
    for i in range(3,n+1):
        code2+=1
        fibo_dp[n] = fibo_dp[i-1]+fibo_dp[i-2] # 코드2
    return fibo_dp[n]
input= sys.stdin.readline

N = int(input())

recursion(N), fibo(N)

print(code1, code2)