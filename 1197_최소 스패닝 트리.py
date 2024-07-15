""" 
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

"""


"""  
첫번째 줄은 정점의 수와 간선의 갯수 (V,E)
두번째 줄부터 간선 정보
A(정점) B(정점) C(가중치)
3 3
1 2 1 : 1->2 로가는 가중치 1
2 3 2 : 2->3 로가는 가중치 2
1 3 3 : 1->3 로가는 가중치 3
"""

""" 
저장해야하는 값
1.각 정점끼리 길이 있는지
2.각 정점간의 비용이 얼마인지
3. 몇번 반복했는지.


데이터를 어떻게 저장하고 어떻게 비교할지 생각해야함.
1. 딕셔너리 형태로 받아온다.
2. 2D array형식으로 받는다.

정점의 크기만큼 테이블을 만든다. [x][y]처럼..
해당 점점으로 갈때 값이 있는지 없는지 비교

"""

def dfs(now,temp_cost,depth):
        
    global cost

    if depth == V-1:
        if temp_cost < cost :
            cost = temp_cost
            return
    
    if temp_cost >= cost :
        return

    for i in range(1,V):
        # print("temp_cost",temp_cost)
        if visited[i]==False and graph[now][i] !=0 :
            visited[i]=True
            dfs(i,graph[now][i]+temp_cost,depth+1)
            visited[i]=False


V, M = map(int,input().split())

graph = [[0]*V for _ in range(V)]
visited = [False] *V
cost = float('inf')
temp_cost = 0
depth = 0


for i in range(M):
    x,y,E = map(int,input().split())
    graph[x-1][y-1] = E
    graph[y-1][x-1] = E

dfs(0,0,0)
print(cost)