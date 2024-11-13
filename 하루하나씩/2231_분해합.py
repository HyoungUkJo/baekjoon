""" 
N이 들어왔을때 각 자리수의 합을 구함
그 자리수와 N을 더함
"""

N = int(input())

tmp = N

resultarr= []

# 여기서 자리수를 나누어야함.
while(1): 
    tmp -= 1        # result를 찾을 값
    tmp2 = tmp      # 슬라이싱때 사용할 값
    result = tmp    # 합을 비교할 값
    sliceNum = []
    if(result == 0):
        break

    while(tmp2>0) :
        sliceNum.append(tmp2%10)
        tmp2= int(tmp2/10)

    for i in sliceNum:
        result += i

    if(N == result):
        resultarr.append(tmp)

if(len(resultarr) == 0):
    print('0')
else : print(min(resultarr))