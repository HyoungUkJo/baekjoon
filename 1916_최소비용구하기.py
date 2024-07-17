import heapq
def dijkstra(start):
    distances[start]=0

    queue = [(0,start)]

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue
            # neighbor 의 0은 다음노드 1은 요금
        for neighbor in graph[node]:
            cost = dist+neighbor[1]
            if cost < distances[neighbor[0]] :
                distances[neighbor[0]]=cost
                heapq.heappush(queue,(cost, neighbor[0]))

    

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distances=[float('inf')]*len(graph)

for _ in range(M):
    s_node, n_node, cost = map(int,input().split())
    # graph[s_node]=[n_node,cost] -> graph[s_node][0]은 (n_node,cost) ->graph[s_node][0][0]은 s_node의 다음 노드이다.
    graph[s_node].append((n_node,cost))

#A->B를 갈 수 있는 경우만 입력한다.
A,B = map(int,input().split())

dijkstra(A)

print(distances[B])