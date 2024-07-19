import time

# 재귀적 방법으로 피보나치 수열 계산
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 동적 계획법으로 피보나치 수열 계산
def fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# 시간 측정을 위한 함수
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# 피보나치 수열의 n 번째 값을 계산하고 실행 시간을 측정
n = int(input())

# 재귀적 방법으로 계산
result_recursive, time_recursive = measure_time(fibonacci_recursive, n)
print(f"Recursive - F({n}): {result_recursive}, Execution Time: {time_recursive:.6f} seconds")

# 동적 계획법으로 계산
result_dp, time_dp = measure_time(fibonacci_dp, n)
print(f"Dynamic Programming - F({n}): {result_dp}, Execution Time: {time_dp:.6f} seconds")
