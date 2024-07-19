import heapq

N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

#distance 초기화
def dijkstra(start):
    distances = [float('inf')]*len(graph)
    distances[start] = 0

    #초기 queue값을 넣어준다. distance가 항상 먼저여야한다.(distance를 기준으로 우선순위 큐를 만듬)
    queue=[(0,start)]

    while queue :
        cur_distance, cur_node = heapq.heappop(queue)
        if cur_distance > distances[cur_node]:
            continue

        for neighbor in graph[cur_node]:
            weight = graph[cur_node][neighbor]
            if weight !=0 : 
                distance = weight+cur_distance
                if distance < distances[neighbor]:
                    distances[neighbor]=distance
                    heapq.heappush(queue,(distance,neighbor))
    
    return distances
    


for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)

distances = dijkstra(X)

isNone=1
for i in range(1,N):
    if distances[i]==K:
        print(i)
        isNone=0
    
if isNone:
    print(-1)