def dfs(start) :
    # global count
    visited[start]= True
    for i in graph[start]:
        if not visited[i] and graph[start]!=0:
            dfs(i)
            # count+=1


N = int(input())
M = int(input())
count =0

graph = [[0] for _ in range(N)]
visited = [False]*(N)
for _ in range(M):
    x,y = map(int,input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

dfs(0)
for i in range(1,N):
    if visited[i]==True:
        count+=1
print(count)

####
""" 
연결리스트들을 확인
연결 리스트에 있는 노드들의 갯수 카운트 하면 될듯
visted[]투르 값 확인
"""
####