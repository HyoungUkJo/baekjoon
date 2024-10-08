N = int(input())
arr = list(map(int, input()))
sum = 0

for i in range(N):
    sum += arr[i]
print(sum)