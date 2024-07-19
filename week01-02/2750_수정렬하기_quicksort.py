#퀵 솔트

""" 
N//2해서 pivort을 정한다.
pl을 0으로 초기화 하고 pr을 N의len으로 설정한다.
반복문으로 탈출 조건을 정한다
while pl<=pr ->pl이 pr보다 작거나 같을경우 반복 즉 pl이 pr보다 더 커질경우 패스 1을 종료한다.

question : 1패스가 종료되었을때 배열을 두가지로 나누어서 진행해야하는데 이떄 어떤식으로 코드를 짤 것인가.
 -> 패스가 종료되었을때 함수를 두번 호출한다 즉 재귀함수를 짠다. 끝났을떄의 기준으로 left값과 rigth값을 넘겨주면 될듯

question : 어떻게 종료 시킬것인가?? 
    guess : 

"""

a=[]

def quick_sort(a,pl,pr) :
    
    pv = a[(pl+pr)//2]
    while pl <= pr :
        while a[pl] < pv : pl +=1
        while a[pr] > pv : pv-=1
        a[pl],a[pr] = a[pr],a[pl] 
    if a[pr] <= a[pl] : 
        a[pr], a[pl] = a[pl], a[pr]
        pr+=1
        pv-=1
    
    quick_sort(a,0,pr)
    quick_sort()
