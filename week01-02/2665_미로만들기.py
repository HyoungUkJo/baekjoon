""" 

""" 
import heapq

def dijkstra(start_x,start_y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = [(0,start_x,start_y)]
    distances[start_x][start_y]=0
    
    while queue :
        cost,x,y = heapq.heappop(queue)
        if cost > distances[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if maze[nx][ny]==1:
                    weight = cost
                else:
                    weight = cost+1
                
                if distances[nx][ny]>weight:
                    distances[nx][ny]=weight
                    heapq.heappush(queue,(weight,nx,ny))
    return distances[N-1][N-1]
            

    



#방의 수 입력 
N=int(input())

distances = [[float('inf')]*N for _ in range(N)]
#미로 입력
maze = [list(map(int, input().strip())) for _ in range(N)]


print(dijkstra(0,0))


