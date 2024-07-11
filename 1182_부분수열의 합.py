# 원소들을 더해서 S가 되는 값을 구한다
# 하나씩 더했을때 확인해보고 두개씩 더했을때 확인해보고 세개씩 더했을때 확인해보고...
# 두 수를 하나씩 찝는다.
# 두수의 차이의 원소를 배열에서 찾는다.
# 세 수의 차이의 원소를 배열에서 찾는다.
# ... N수의 차이의 원소를 배열에서 찾는다.
# 재귀 일 것 같은데...;;;
# 인솔트 해서 첫번째 값과 마지막 값이 원하는 수보다 작으면 left와 right의 간격을 줄여서 비교해야하나???
# mid 값을 기준으로 해서 본인이 S 보다 크면 rigt를 mid로 해서 하나씩 더해보는것?
# 본인이 작으면 left를 mid로 해서 비교할것
# 첫번째 
def sum_jegui(a,S,n) :
    # 값 두개끼리 비교했을떄 같으면 리턴 1 못찾으면 0
    #값 3개끼리 비교했을떄
    # 값 4개끼리 비교했을떄 ~~~~~~~~
    if n < 0 : return 0

    else : a[n] + 

    if a[i]+a[j]==S:
        a.pop(a[i])
        a.pop(a[j])


NS = list(map(int,input().split()))
N=NS[0]
S=NS[1]

oneso = list(map(int,input().split()))
oneso.sort()
""" 
# 이진 탐색?
left = 0
right = len(oneso)-1
while left <= right:
    mid = (left+right)//2

    if mid < S :
        left = """



for i in range(len(oneso)):
    for j in range(i,len(oneso)):
        oneso[]