N,K = map(int,input().split())

arr=[]

for _ in range(N):
    a = int(input())
    arr.append(a)

count=0
for i in range(N-1,-1,-1):
    while K>0:
        # print("i",i)
        # print(f'i={i} K={K} arr:{arr[i]},count={count}')
        if arr[i] <= K:
            K-=arr[i]
            count+=1
        else : break
print(count)