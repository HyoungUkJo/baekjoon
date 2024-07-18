""" 
1. 3차원 배열 입력
2. 현재 익은사과(1) 부터 시작
2.1. 익은사과를 찾아서 큐에 미리 넣어놔야지...
3. 상하좌우앞뒤 비교
4. 반복
5. 
 """
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx = [0,0,-1,1,0,0]
    dy = [0,0,0,0,-1,1]
    dz = [-1,1,0,0,0,0]



    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if matrix[nz][nx][ny] ==0:
                    matrix[nz][nx][ny] = matrix[z][x][y]+1
                    queue.append((nz,nx,ny))


queue = deque()
m,n,h = map(int,input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# visited = [[[0]*m for _ in range(n)]for _ in range(h)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k]==1:
                queue.append((i,j,k))
bfs()
check=False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k]==0:
                check=True
            else: day = max(day,matrix[i][j][k])
# print(matrix)
if check:
    print(-1)
else:
    print(day-1)
