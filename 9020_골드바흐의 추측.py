import math
#소수인지 판별하는 함수
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True
#판별한 소수를 리스트에 저장
def savePrimes(num) :
  prime=[]
  for i in range(num+1):
    if isPrime(i):
      prime.append(i)
  return prime
#소수를 찾는 함수
def find_Prime_sum(num) :
  prime=[]
  prime = savePrimes(num)
  flag = 0
  #소수의 절반만큼만 돌리기 위해서 사용
  for i in range(int(math.sqrt(num)),0,-1) :
    # print(int(math.sqrt(num)))
    for j in range(int(math.sqrt(num)),0,-1) :
      if prime[i] + prime[j] == num :
        print(prime[j],prime[i])
        flag =1
        break
    if flag==1:
      break

N=int(input())
num = list(map(int,input().split()))
# print(N)
for i in num:
  find_Prime_sum(i)

