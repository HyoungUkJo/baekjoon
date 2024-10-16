N,M = map(int,input().split())


arrA = list(map(int,input().split()))
    
arrB = list(map(int,input().split()))


arrSum = arrA+arrB
arrSum.sort()

print(*arrSum)