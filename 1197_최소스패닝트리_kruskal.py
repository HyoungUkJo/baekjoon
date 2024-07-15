"""  

"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트노드를 찾을때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 정점과 간선의 갯수를 입력받음
V, E = map(int,input().split())
# 부모 테이블의 초기화 (V+1을 하는 이유??)
# 부모테이블이 있어야 하는 이유? -> 사이클이 있는지 아닌지 확인하기 위함??
parent = [0] * (V+1)

# 간선과 간선의 비용 저장
edges = []
result=0

#부모 테이블 자기 자신으로 초기화
for i in range(1,V+1):
    parent[i]=i
print(parent)
#모든 간선에 대한 정보 입력
count=0
for _ in range(E):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

#간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않은 경우에만 집합에 포함. -> 부모가 다를경우에만 포함?
    print(f'parent:{parent}, a:{a} b:{b}')
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += cost

print(result)