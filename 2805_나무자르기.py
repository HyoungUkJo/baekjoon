#
#

""" 



입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

1.톱의 길이는 1 부터 max(trea) 다
2. 우리는 중간 기준을 찾기 위해 중간 지점을 찾는다. 
3. 톱의 중간지점을 잡고 톱보다 큰것들을 잘라서 sum에 저장한다.
4. 만약 sum 이 M 보다 클 경우 top = top+1 -> 더 빨리 찾아갈 수있는 수식을 찾아야할듯
5. 반복



"""
N,M = map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()

low, high = 0, max(tree)
top = (low + high) // 2

while low <= high :
    branch=0
    # print(top)
    for i in tree :        
        if i > top:
            branch += i - top
        
    if branch >= M :
        low = top +1
    else:
        high = top -1

print(high)