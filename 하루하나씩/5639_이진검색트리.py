import sys
sys.setrecursionlimit(10 ** 5)

input= sys.stdin.readline

def tree(arr):
    left = []
    right= []
    if len(arr)==0 :
        return
    mid = arr[0]
    for i in range(1,len(arr)):
        if mid<arr[i]:
            left=arr[1:i]
            right=arr[i:]
            break
        else :
            left=arr[1:]
    tree(left)
    tree(right)
    print(mid)

arr = []

while True:
    try:
        a = int(input())
        arr.append(a)
    except:
        break
tree(arr)