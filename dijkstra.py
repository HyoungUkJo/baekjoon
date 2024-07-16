"""  
다익스트라 알고리즘은 시작정점에서 다른 모든 정점으로의 최딘 경로를 찾는데 사용이 된다.

다익스트라 알고리즘 풀이방법
1. 시작정점설정
2.미방문 정점 집합 유지 : 
    - 그래프의 모든 정점을 미방문 접점에 유지시킨다.
3. 현재 정점 선택 : 
    시작정점부터 출발해서 현재 정점을 선택한다.
    처음에는 시작점이 현재 정점이다.
4. 이웃 정점 업데이트
    현재 정점과 연결된 모든 이웃 정점에 대해 현재 경로를 선택해서 가면 더 빠를 시 업데이트한다.
5. 방문한 정점 표시
    현재 정점을 미방문 정점에서 제거
6. 마방문 정점 집합이 비워지지 않았을 경우 4번부터 반복


"""

import heapq

def dijkstra(graph, start):
    # 시작 정점부터의 최단 경로를 저장하는 딕셔너리
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 우선순위 큐
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 현재 노드의 최단 경로가 이미 갱신된 경우 무시
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로를 발견한 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 그래프를 딕셔너리로 표현
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 알고리즘 실행
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
