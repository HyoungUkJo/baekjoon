# 카운트를 어떻게 할 것이냐??? 나는 그냥 변수로 하면 될것같은데... count +=1 이런식
# 미로의 바깥을 벗어나면 안된다.
# 갔던곳을 또 방문해서는 안된다.
# 벽이 있는곳은 갈 수 없다.

from collections import deque

# Bfs를 통해서 최단 경로를 확인한다.
def bfs(start_x, start_y):
    #첫번째 들어온 값을 초기화
    global N,M
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x,start_y)])
    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4) :
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:  # 범위 확인
                if maze[nx][ny] == 1:  # 경로 확인
                    queue.append((nx,ny))
                    maze[nx][ny]=maze[cur_x][cur_y]+1
    print(maze[N-1][M-1])


N, M = map(int,input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

distance =[[]*M for _ in range(N)] 
visited = [[False]*M for _ in range(N)]


bfs(0,0)


""" 
# 카운트를 어떻게 할 것이냐??? 나는 그냥 변수로 하면 될것같은데... count +=1 이런식
# 미로의 바깥을 벗어나면 안된다.
# 갔던곳을 또 방문해서는 안된다.
# 벽이 있는곳은 갈 수 없다.

from collections import deque

# Bfs를 통해서 최단 경로를 확인한다.
def bfs(start_x, start_y):
    #첫번째 들어온 값을 초기화
    global N,M
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x,start_y)])
    max_x = N
    max_y = M

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:  # 범위 확인
                if maze[next_x][next_y] == 1:  # 경로 확인
                    queue.append((next_x, next_y))
                    maze[next_x][next_y] = maze[x][y] + 1  # value 자체를 이동 횟수로 사용

    print(maze[N-1][M-1])


N, M = map(int,input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

distance =[[]*M for _ in range(N)] 
visited = [[False]*M for _ in range(N)]

bfs(0,0)
# print(result)

 """