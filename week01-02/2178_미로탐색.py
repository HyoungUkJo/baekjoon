""" 
NXM크기의 배열의 미로가 있다.

"""
from collections import deque

def bfs(start_x, start_y, graph):
    count =0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x,start_y)])
    visited = [[False]*M for _ in range(N)]
    visited[start_x][start_y]=True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<len(graph) and 0<= ny < len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny]=True
                    count+=1
                    queue.append((nx,ny))
                    if nx == N - 1 and ny == M - 1:
                        return count
    return count
    

N,M = map(int,input().split())
# split이 아니라 strip으로 각 자리를 다 쪼개서 리스트로 보낸다.
maze = [list(map(int, input().strip())) for _ in range(N)]
# print(map)
result = bfs(0,0,maze)

print(result)