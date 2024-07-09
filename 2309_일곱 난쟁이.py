""" 
문제
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

입력
아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

출력
일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
"""

# 완전탐색을 통해 원하는 값이 있을때 까지 배열을 뒤지자
# 1. 9개의 배열을 받는다.
# 2. 정렬을 한다.
# 3. 문자열의 총 합을 구한다.
# 4. 100에서 빼 값을 sub에저장한다.
# 5. sub와 같은 값을 이중 for문을 통해서 찾는다.
# 6. 같은 값이 나온 인덱스들을 반환한다.
# 

def find_nangeng(arr) :
    result = sum(arr)-100
    for i in range(0,len(arr)-1):
        j=i
        for j in range(j,len(arr)):
            if arr[i] + arr[j]==result:
                return i, j
    return 0,0
N=[]
for _ in range(9):
    num = int(input())
    N.append(num)
N.sort()

nangeng1 ,nangeng2 = find_nangeng(N)
# N.pop(nangeng1)
# N.pop(nangeng2)
for i in range(9) :
    if i ==nangeng1 or i == nangeng2:
        continue
    print(N[i])




