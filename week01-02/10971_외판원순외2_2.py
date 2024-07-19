# 방문한 나라의 방문 여부는 TRUE FALSE로 판별한다.
"""   
재귀의 분기 조건
1. 만약 내가 들린 횟수가 N이라면 첫번째 값으로 돌아간다.
2. 내가 방문한 나라인지?
3. 다음으로 갈 나라가 있는지?
재귀 복귀는 return cost를 한다.
재귀 탈출 시 
"""

def dfs(now, N, depth, temp_cost):
    global cost

    if depth == N-1:
        if a[now][0] != 0:
            temp_cost += a[now][0]
            if temp_cost<cost:
                cost = temp_cost
        return
    

    # for 문으로 가야할 도시의 값을 1씩 증가
    
    if temp_cost >= cost :
        return

    for i in range(1,N): # 내 지금 도시는 0 임으로 1부터 시작한다.
        #만약 내가 지금 가려는 도시가 방문하지 않은 나라일 시
        if visited[i] == 0 and a[now][i] != 0:  
            # 내가 지금 방문한 국가를 넣는다.
            visited[i]=1
            dfs(i,N,depth+1,temp_cost+a[now][i])
            # 복귀 시 내가 방문한 국가를 return 한다.
            visited[i]=0


if __name__ == "__main__" :
    N = int(input())
    a = [list(map(int, input().split()))for _ in range(N)]
    cost = float('inf')
    visited = [0]*N
    visited[0]=1

    dfs(0,N,0,0)
    print(cost)