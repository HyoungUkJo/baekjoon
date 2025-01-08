# https://app.codility.com/demo/results/trainingJSWQH4-NBT/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    # 빠진 숫자 찾기
    # 반복문으로 돌아야하나.. 그러면 찾을수는 있는데 너무 오래걸리는거아닌가.
    # 최악의 경우 O(N^2)이 될것같다.
    # N이 0일경우도 옴(예외처리 필요)

    # 정상일때와 아닐떄의 차이를 구하면 된다. 이럴떄는 O(2N)인것같다.

    sumA = sum(A)
    
    testSum =0
    for i in range(1,len(A)+2):
        testSum+=i
    
    result = testSum-sumA

    return result