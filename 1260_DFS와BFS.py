"""  
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


"""

""" 
정점의 갯수 =N
탐색 시작 정점 = V
간선이 연결하는 두 정점의 표 :M

어떤식으로 저장해야하나????
시작정점을 출려갛면 되나???
들어갔는지 안갔는지 체크는 visited =[]*N으로 하면 될것같고

"""
from collections import deque

""" 
재귀 조건에 대해서

V=1이라는 가정
1. 첫번째 들어간 V=1을 출력
2-0. 만약 방문하지 않았고 다음 방문할 값이 있다면 -> graph의 해당 배열에서 1이 있는지 없는지로 확인!
2. 첫번째 그래프에 들어가있는 값 중 1로 표기 된 값으로 이동한다.
3. 1로표기된 값으로 이동 -> 본인의 값 출력
4. 본인의 그래프에서 1로 표기되어 있는 값으로 이동
5. 반복
"""


def dfs(now):
    #재귀 함수를 통해서 진행
    visited[now]=1
    print(now+1, end=" ")
    for i in range(N):
        if visited[i]==0 and graph[now][i]==1:
            dfs(i)
    
def bfs(start) :
    queue = deque([start])
    visited[start]=1
    
    while queue :
        now = queue.popleft()
        print(now+1, end=" ")
        for i in range(N):
            if visited[i] != 1 and graph[now][i] ==1:
                queue.append(i)
                visited[i]=1





N,M,V=map(int,input().split())
graph = [[False] * N for _ in range(N)]
visited=[0]*N
for i in range(M):
    x,y=map(int,input().split())
    graph[x-1][y-1]=1
    graph[y-1][x-1]=1
    
dfs(V-1)
visited=[0]*N
print()
bfs(V-1)
# bfs(V,graph)

# arr = [list(map(int, input().split()))for _ in range(5)]