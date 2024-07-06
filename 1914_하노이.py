""" 

문제 푸는중...

 """

def hano (n) :
    if (n==1) :
        return n
    else:
        return 2**(n-1)+hano(n-1)
    
N = int(input())
if N >= 20 :
    print(hano(N))

    # 내가 N일때 내 위치가 1이면
    #N-1은 2로가 나는 3으로갈게
# 내 위치가 2이면
    #N-1은 1로가 나는 3으로 갈게


def move(n,now):
    if n >1 :
        after = 3-now
        if now ==1 :
            move(n-1,now=after)
        elif now ==2 :
            move(n-1, now=after)
            
        print("%d번블록 %d에서 %d으로 이동" %(n,now,after))        


    if n==1:
        print("1번블록 %d번으로 이동 ")

N=int(input())
print(move(N,1))    