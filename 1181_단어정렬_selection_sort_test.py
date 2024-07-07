""" 
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.

"""

# 입력된 문자열의 길이를 저장하는 배열 생성
# 배열의 크기에 맞게 insort()함수를 이용해서 정렬
# -> 삽입 정렬은 이미 정렬된 데이터 속에서 사용할 때 유용함으로 선택정렬을 하는게 유용할듯!! (욱현님 의견)
# 삽입정렬으로 처음에 최초값을 최소로정하고 이후에 들어온 값을 비교해서 정렬할 수 있게
# 나의 뜨거운 마음을~ 불같은 나의 마음을 보여주겠습니다!

from typing import MutableSequence
def selection_sort(a: MutableSequence) :
    n = len(a)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1,n-1):
            print(a[j],a[min_index])
            if len(a[j]) < len(a[min_index]) :
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


N=int(input())
x = [None] * N

for i in range(N) :
    num = input()
    for j in range(i) :
        if x[j]==x[i] :
            continue
        else : x[i] = num

selection_sort(x)

print(x)

