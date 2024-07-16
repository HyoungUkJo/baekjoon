"""  
첫번째는 테스트 케이스의 갯수를 의미한다. K
다음줄에는 테스트 케이스의 정점의 갯수와 간선의 갯수를 받는다. V, E
다음줄에는 간선에 대한 정보가 나온다.
E만큼 정보를 받는다
K 만큼 반복한다.

이분그래프인지 아닌지 확인하는 코드를 작성한다.

이분 그래프의 그룹을 나누어야 한다. visited로 1로 visited를 할지 -1로 visited를 할지 정하자

dfs 에서 비교연산을 같이 해버린다면?????

"""
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(start, group):

    visited[start]=group
    
    for i in graph[start]:
        if visited[i]==0:
            result = dfs(i, -group)
            if not result:
                return False
        else:
            if visited[i]==group:
                return False
    return True

K = int(input())

# K 번 반복해야하니 이렇게.. 함수로 찢어서 하는게 나으려나??
for _ in range(K):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    
    for _ in range(E):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1,V+1):
        if visited[i] == 0:
            result = (dfs(i, 1))
            if not result :
                break
    print("YES") if result else print("NO")


