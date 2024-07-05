T = int(input())
for a in range(T):
    R,S = input().split()
    R=int(R)
    P=""
    for j in S :
        str = j*R
        P+=str
    print(P)
