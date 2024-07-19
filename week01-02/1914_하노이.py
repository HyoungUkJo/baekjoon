""" 
하노이탑풀이
1. 현재 내 위치를 확인 할 줄알아야함.
2. 나는 결국은 통으로 위에 있는 친구들을 옮겨야함.
3. 재귀로 스택에 print가 쌓아지는 방식으로 가보자

"""

def hano(no,now,after) :

    if no >1 :
        hano(no-1, now,6-now-after)
    
    # print(f'{no}번째 원반 {now}에서 {after}로 이동')
    print(now,after)
    
    if no >1 :
        hano(no-1, 6-now-after,after)

def hano_culc(n) :
    if n ==1:
        return n
    elif n>1:
        return hano_culc(n-1)*2+1
    
N= int(input())

if N>20 :
    print(hano_culc(N))
    # print(2**(N)-1)
else:
    # print(2**(N)-1)
    print(hano_culc(N))
    hano(N,1,3)
    


