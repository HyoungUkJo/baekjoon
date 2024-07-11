# 골드바흐의 추측
# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 먼저 들어온 수의 소수를 찾는다.
# 소수를 저장하고 중간값을 설정한다.
# 중간 친구와 수를 빼면 소수가 나오지 않을까? 라는 생각을 해보면서 일단 풀어보자.
# 

# 에라토스테네스의 채 알고리즘

import sys
input=sys.stdin.readline
def isPrime(a):
  if a < 2:
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def savePrimes(num) :
  prime=[]
  for i in range(num+1):
    if isPrime(i):
      prime.append(i)
  return prime

def findPrime(num,prime):
    mid = len(prime)//2
    for i in range(mid, -1, -1):
      for j in range(mid, len(prime)):
        if prime[i] + prime[j] == num :
            print(prime[i],prime[j])
            return
        if prime[i] + prime[j] >= num :
            break

N=int(input())
arr = []
for i in range(N) :
  num = int(input())
  arr.append(num)

for i in range(N):
  prime_arr = savePrimes(arr[i])
  findPrime(arr[i],prime_arr)




