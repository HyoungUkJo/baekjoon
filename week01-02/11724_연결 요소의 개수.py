"""  
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ Nx(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

"""
from collections import deque


def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited[start] = True

    queue = deque([start])

    while queue :
        curr_node = queue.popleft()

        for i in graph[curr_node]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    


N,M = map(int,input().split())

graph = [[0]for _ in range (N+1)]
visited = [False]*(N+1)

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

count=0

for i in range(1,N+1):
    if not visited[i]:
        # dfs(i)
        bfs(i)
        count+=1
print(count)





