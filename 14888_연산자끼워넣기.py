
N = int(input())
num = list(map(int,input().split()))
operator= list(map(int,input().split()))
min_sum = int(1e9)
max_sum = int(-1e9)

def dfs(depth,tmp_sum):

    global min_sum,max_sum

    if depth == N-1:
        if max_sum < tmp_sum :
            max_sum = tmp_sum
        if min_sum > tmp_sum :
            min_sum = tmp_sum
        return
    
    if operator[0] != 0:
        operator[0] -=1
        dfs(depth+1,tmp_sum + num[depth+1])
        operator[0] +=1
    
    if operator[1] != 0:
        operator[1] -=1
        dfs(depth+1,tmp_sum - num[depth+1])
        operator[1] +=1
    
    if operator[2] != 0:
        operator[2] -=1
        dfs(depth+1,tmp_sum * num[depth+1])
        operator[2] +=1
    
    if operator[3] != 0:
        operator[3] -=1
        dfs(depth+1,int(tmp_sum / num[depth+1]))
        operator[3] +=1


dfs(0,num[0])
print(max_sum)
print(min_sum)
