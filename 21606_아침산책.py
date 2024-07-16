""" 
산책을 위한 경로 중간 지점을 만들어 놨는데 중간 지점을 두번 거치지 않고 도착점까지 가는것
0으로 표기된 값은 실내이다. 실내는 무조건 마지막이나 첫번째에 들릴 수 있도록 한다.
우리는 이런 서로 다른 선택지의 경로가 몇개가 있는지 구해야한다. ok?
해결해야할 문제
들어가려는 노드가 실내인지 실외인지 확인
    1. 실외일시 : 깊이만큼 가지 않았을때 실내를 만났을 경우 해당 경로로 가지 않는다.
    2. 실내일시 : 깊이만큼 가지 않았을때 실외를 만났을 경우 해당 경로로 가지 않는다.

 """
 

def dfs(start):
    for i in graph[start]:
        if not visited[start] and graph[start][i]!=0:



N = int(input())
A = list(input())

place=[0]
place.append(A)

visited = [False] * (N+1)

graph = [[]for _ in range(N+1)]

for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,N+1):
    dfs(i)