""" 
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


첫째줄에 수 입력
첫째줄에 받은 수만큼 입력
쉘정렬은 받은 수를 나누어서 그만큼 나누어서 처리한다.

"""

def quation_book(arr):       
    h = len(arr)//2

    while h>0 :
        for i in range(h,N) :
            j = i
            while j>= h and arr[j-h] > arr[j] :
                arr[j-h], arr[j] = arr[j], arr[j-h]
                j -= h
        h//=2
    for i in range(N):
        print(arr[i])

def only_my_shellsort(arr):
    h = len(arr)//2

    while h>0 :    
        for i in range(0,h):
            # print(f'{i}:{arr}')
            for i in range(h+1) :
                if arr[i] > arr[i+h] :
                    arr[i], arr[h+i] = arr[h+i],arr[i]
        h//=2
    for i in range(N):
        print(arr[i])


N=int(input())

arr=[]
for _ in range(N) :
    num = int(input())
    arr.append(num)


### h만큼 떨어진 원소끼리 비교한다.

#첫번째 수와 첫번쨰 수 +H의 수 비교
#첫번쨰 수가 더 크면 스위치

#두번째 수와 두번째 수 +h의 수 비교
# 두번쨰 수가 더 크면 스위치
# ...
quation_book(arr)
only_my_shellsort(arr)