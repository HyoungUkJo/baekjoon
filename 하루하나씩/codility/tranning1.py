# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    
    # N을 이진수로 바꾼다.
    # 1이나왔을 경우 max와 현재 이진 간격을 비교한다.
    # 0이 나왔을 경우 현재 이진 간격을 + 한다.
    # 만약 1이 나오면 현재 이진 간격과 max 이진간격을 비교해서 더 큰걸 max로 저장
    # 1이 나오기 전의 0을 카운트 하지 않기 위해 Flag를 만든다.
    flag = False
    tempBinary=0
    maxBinary=0
    while N !=0 :
        value = N%2
        if value == 0 :
            tempBinary+=1
        else:
            if flag==False:
                tempBinary=0
            flag=True
            maxBinary=max(maxBinary,tempBinary)
            tempBinary=0
        N=N//2
    
    return maxBinary