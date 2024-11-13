# N장의 카드중 3장을 골라 M을 넘지않는 수중 가장 가까운 수를를 만들어라

N,M = map(int,input().split())

card = list(map(int,input().split()))

sumArr = []
# 3번의 반복문을 통해서 근사값을 구한다.

for i in range(N) :
    for j in range(i+1,N):
        for z in range(j+1,N):
            sum = card[i]+card[j]+card[z]
            if(sum > M):
                continue
            sumArr.append(sum)

print(max(sumArr))

