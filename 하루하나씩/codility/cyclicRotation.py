# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def cycle(A):
    tempNum = A[-1]
    for i in range(len(A)-1,0,-1):
        A[i]=A[i-1]
    A[0]=tempNum
    return A
def solution(A, K):
    # A는 배열로 주어진다.
    # K는 A를 몇번 오른쪽으로 이동시킬지를 나타낸다.
    
    # 맨 마지막 값을 임시값으로 저장
    # 옆으로 한칸씩 값을 덮어씌우는 반복문 실행
    # 만약 배열의 크기와 K 가 같다면 그대로 출력
    # 만약 같은 숫자로만 이루워져있다면 그대로 출력
    # 배열을 set함수로 돌려서 만약 1이 나올경우 그대로 출력

    setA_Size =len(set(A))
    if setA_Size == 1:
        return A
    elif K == len(A):
        return A
    elif len(A)<=1:
        return A
    for i in range(K):
        A=cycle(A)  

    return A