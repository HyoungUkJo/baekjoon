""" 
풀이를 안보고 풀어보기!!

내가 문을 했는지 체크, 나랑 이어져 있는지 확인

DFS : 이어져 있는 값중 가장 먼저 들어 있는 값으로 이동
BFS : 이여저 있는 값들을 큐에 append 후 하나씩 pop

(정답은 안다.. 그래프를 아차원 배열로 만들고 해당 배열이 이어져있는지 확인하면 되는데
이런 생각을 못하겠다...)
값을 두개씩 줄때 이렇게 생각해야하나?? 지금은 두개인데 3개를 주면 어떻게 생각해야하는지??
판은 바뀌는게 없을 것 같은데 받아서 어떻게 처리를 해야하는지 생각은 필요할 것 같다.

"""

from collections import deque

def dfs(now):
    visited[now]=1 # 한번 들어간 값을 다시 들어가지 않을것이기 때문에 바로 저장
    print(now+1, end=" ")
    for i in range (N) :
        if visited[i]==0 and graph[now][i]==1:
            dfs(i)


# 큐에 저장하는 방식이죠~
def bfs(now):
    queue = deque([now])
    visited[now]=1
    while queue:
        curr_node = queue.popleft()
        print(curr_node+1, end=" ")
        for i in range(N):
            if visited[i]==0 and graph[curr_node][i]==1:
                queue.append(i)
                visited[i]=1


    



N, M, V= map(int,input().split())

graph=[[0]*N for _ in range(N)]

for i in range(M):
    x, y = map(int,input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

visited = [0]*N

dfs(V-1)
visited = [0]*N
print()
bfs(V-1)


