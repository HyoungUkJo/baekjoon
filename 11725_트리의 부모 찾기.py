"""  
루트 없는 트리가 주어진다.
이때 트리의 루트를 1로 가정할때 각 노드의 부모를 구하는 프로그램 작성

각 부모를 어떻게 찾을것인지

1번루트에서 나온 친구들은 부모이다.
부모 아래 있는 친구들은 부모이다.
부모아래 아무것도 없다면 부모가 아니다.
    -> 이걸어떻게 확인할지 생각해봐야함.


"""

from collections import deque

def bfs(start):
    queue = deque([start])
    parents[start] = start
    while queue :
        cur_node = queue.popleft()

        for child in graph[cur_node]:
            if parents[child]==0:
                parents[child]=cur_node
                queue.append(child)

            


def dfs(start):
    children = graph[start]

    for i in children:
        if parents[i]==0:
            parents[i]=start
            dfs(i)


N = int(input())

graph = [[0] for _ in range(N+1)]
parents = [0] * (N+1)
parents[1]=1

for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
# dfs(1)

for i in range(2,N+1):
    print(parents[i])