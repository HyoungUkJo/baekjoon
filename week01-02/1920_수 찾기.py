N = int(input())

comp_list = []

comp_list=list(map(int,input().split()))

## 들어온 리스트를 sort 해서 정렬해줘야함
comp_list.sort()
##


M = int(input())

arr = []

arr=list(map(int,input().split()))

#####
""" 
비교 값을 중간으로 쪼갠다 -> N//2
중간으로 쪼갠 값보다 작을경우
 (작을경우) Mid 의 오른쪽 버린다.
 (클경우) Mid의 왼쪽 버린다.
 (같을경우) 반환~

 comp_list의 가장 왼쪽을 pl 가장 오른쪽을 pr로 지정한다.
 Mid의 오른쪽을 버리면 Mid+1은 pl이 된다.
 Mid의 왼쪽을 버리면 Mid-1은 pr이 된다.



 이것도 인덱스가 중요할듯!!
"""
####

def binary_search(arr, x):
    pl = 0
    pr = len(arr) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        mid = arr[pc]
        
        if mid == x:
            return 1
        elif mid < x:
            pl = pc + 1
        else:
            pr = pc - 1

    return 0

for num in arr:
    print(binary_search(comp_list, num))


    
