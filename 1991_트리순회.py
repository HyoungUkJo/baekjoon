###
""" 
어떤식으로 풀어야 할까??
dfs로 푼다면..
일단 테이블을 먼저 만들어야하나??
그리고 전위 순해는 하던대로 하면 될듯하고
테이블을 N=1크기만큼 만들어서 [0]값에는 알파벳을 넣는게 나으려나?
"""

N=int(input())


## 딕셔너리(사전형)을 이용한 풀이
tree ={}

for _ in range(N):
    root,left,right = input().split()

    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root!='.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

def postorder(root):
    if root !='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
        


