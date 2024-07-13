""" 
NXM크기의 배열의 미로가 있다.

"""
from collections import deque

def bfs(start_x, start_y, graph):
    count =0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x,start_y)])
    visited = set([(start_x,start_y)])
    print("firstQ",)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

        if 0<=nx<len(graph) and 0<= ny < len(graph[0]):
            if (nx,ny) not in visited and graph[nx][ny]!=0:
                visited.add((nx,ny))
                queue.append((nx,ny))
                count+=1
    return count
    

N,M = map(int,input().split())
# split이 아니라 strip으로 각 자리를 다 쪼개서 리스트로 보낸다.
map = [list(map(int, input().strip())) for _ in range(N)]
# print(map)
bfs(0,0,map)
