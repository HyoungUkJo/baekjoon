"""  
외판원 순회 진짜 찐찐막

각 도시를 순회하는 최단거리를 구해야함.

이차원 배열

조건 :
1. for 문을 이용해서 순회하는데 만약 방문한 도시는 넘긴다. 길이 없는 도시도 넘긴다.
2. 비용을 계산해서 가장 최저값을 출력한다.
3. 만약 마지막 도시에 방문했을때는 무조건 첫번째 도시로 돌아간다.

재귀하는데 무엇이 필요할까??
3. 다음으로 가는 도시가 어디인지?
1. 몇번 순회 했는지
2. 지금까지 비용이 얼마가 들었는지



"""

def dfs(now, depth, temp_cost):

    global cost

    if depth == N-1 :
        if arr[now][0]!=0 :
            temp_cost+=arr[now][0]
            if cost > temp_cost :
                cost = temp_cost
        return

    if temp_cost >= cost :
        return

    for i in range(1,N):
        if visited[i]==0 and arr[now][i] !=0 :
            visited[i]=1
            dfs(i,depth+1,temp_cost+arr[now][i])
            visited[i]=0 # 배열이기 때문에 복귀 시 원복시켜줘야한다.. 아니면 for문이 계속 돌때마다 모든 수가 1이되는 극악의 상황이 발생한다.




N=int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
cost = float('inf')
visited = [0]*N
visited[0] =1
dfs(0,0,0)
print(cost)