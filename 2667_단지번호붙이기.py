from collections import deque

def bfs(dan,start_x, start_y):
    visited[start_x][start_y]=dan

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x,start_y)])
    count =1
    while queue:
        # print(queue)
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]!=0 and visited[nx][ny]==0:
                    visited[nx][ny]=dan
                    count+=1
                    queue.append((nx,ny))
    return count


N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dan=0
counts=[]

for i in range (N):
    for j in range(N):
        if graph[i][j]==1 and visited[i][j]==0:
            dan+=1
            counts.append(bfs(dan,i,j))

print(dan)
counts.sort()
for i in counts:
    print(i)

