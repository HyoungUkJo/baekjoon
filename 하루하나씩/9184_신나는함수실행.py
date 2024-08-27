memo = [[[0]*21 for _ in range(21)] for _ in range(21)]
def w(x,y,z, memo):
    
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    else :
        if x >20 or y > 20 or z > 20:
            memo[20][20][20] = w(20,20,20, memo)
            return memo[20][20][20]
        if memo[x][y][z] != 0:
            return memo[x][y][z]
        if x < y < z:
            memo[x][y][z] = w(x,y,z-1, memo) + w(x,y-1,z-1, memo) - w(x,y-1,z, memo)
            return memo[x][y][z]
        else :
            memo[x][y][z] = w(x-1, y, z , memo) + w(x-1, y-1, z, memo) + w(x-1, y, z-1, memo) - w(x-1, y-1, z-1, memo)
            return memo[x][y][z]
while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d"%(a,b,c, w(a,b,c, memo)))