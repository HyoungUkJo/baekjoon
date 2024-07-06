##팩토리얼 문제 풀이법
# 먼저 입력된 수에서 1을 뺀 수만큼 반복
# 재귀를 써서 풀이 가능할듯
def facto(n) :
    if n<=1 :
        return 1
    return n*facto(n-1)
N = int(input())

result = facto(N)
print(result)
