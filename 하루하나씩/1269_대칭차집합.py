N, M = map(int, input().split())

n,m = N, M

arrA = set(list(map(int,input().split())))
# arrA.sort()
arrB = set(list(map(int,input().split())))
# arrB.sort()

inter = (arrA|arrB) - (arrA&arrB)

print(len(inter))


""" 
for i in range(N):
    if(i>=M):
        break
    if(arrA[i]==arrB[i]):
        n-=1

for j in range(M):
    if(j>=N):
        break
    if(arrB[i]==arrA[i]):
        m-=1
print(n+m) """