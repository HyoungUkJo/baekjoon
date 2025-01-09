""" 
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

"""
# 깊이우선탐색 -> 끝까지 먼저 들어가기
def dfs(idx):
    global table
    table[idx]=True
    print(idx, end=" ")
    for next in range(1,N+1):
        if not table[next] and graph[idx][next]:
            dfs(next)

# 너비우선탐색 -> 같은열부터 반복하기
def bfs(idx):
    global table
    global q
    while q:
        cur = q.pop(0)
        print(cur,end=" ")
        for next in range(1,N+1):
            if not table[next] and graph[cur][next]:
                table[next]=True
                q.append(next)


import sys

# NMV입력받기
N,M,V = map(int, input().split())

# M개의 줄에 두 정점의 번호가 주어짐
# 정점의 정보를 저장할 그래프 2차원배열 생성
graph = [[False]*(N+1) for _ in range(N+1)]
table = [False]*(N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# V부터 방문
# dfs
dfs(V)
# bfs
print()
table = [False]*(N+1)
q=[V]
table[V]=True
bfs(V)


