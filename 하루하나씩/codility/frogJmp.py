#1st test : https://app.codility.com/demo/results/training8Z5TAH-VT8/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # X에 D만큼 더했을때 몇번 더해야 Y보다 같거나 크냐? 라는 문제

    i=0
    while(X<Y):
        X+=D
        i+=1
    return i

# 2nd test : https://app.codility.com/demo/results/trainingVRJP2Q-Y7R/
def solution(X, Y, D):
    Y-=X

    i = Y//D
    if(Y%D!=0):
        i+=1
    return i
