arr = []
for i in range(9) :
    num = int(input())
    arr.append(num)
max_num = max(arr)
max_index = arr.index(max_num)+1
print(max_num)
print(max_index)


"""
arr=list(map(int,input().split()))
max_num = max(arr)
print(max_num)
print(arr.index(max_num)+1)



##########################################3

arr=list(map(int,input().split()))

max = 0

for i,value in enumerate(arr) :
    if value >max :
        max = value
        max_index = i+1
print(max)
print(max_index)


"""