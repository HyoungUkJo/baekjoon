express = input().split('-')

result=[]


for i in express:
    tmp=i.split('+')
    sum=0
    for j in tmp:
        print(sum,j,result)
        sum+=int(j)
        
    result.append(sum)
# reulst에 저장
sum=0
for i in result:
    sum-=int(i)
print(sum)