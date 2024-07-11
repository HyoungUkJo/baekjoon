N = int(input())
# M = N
if N < 10:
    N = N * 10  
i = 0
M = N

while True:
    a = M % 10
    b = M // 10
    c = (a + b) % 10
    M = (a * 10) + c
    i += 1
    if M == N:
        break

print(i)