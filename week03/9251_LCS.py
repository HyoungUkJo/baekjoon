str1 = list(input())
str2 = list(input())

# 문자열을 배열로 만들어야함.
dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        dp[i][j]=dp[i-1][j]
        if dp[i][j] < dp[i][j-1]:
            dp[i][j] = dp[i][j-1]
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
"""         if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) """
# print(dp)
# print(str1)
# print(len(str1))
print(dp[len(str1)][len(str2)])
# print(max(map(max,dp)))