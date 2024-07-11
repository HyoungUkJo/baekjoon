import math
#소수인지 판별하는 함수
def is_prime_number(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    
    return True

N=int(input())
num = list(map(int,input().split()))

A = num //2
B = num //2

