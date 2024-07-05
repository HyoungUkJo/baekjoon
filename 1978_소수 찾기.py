N = int(input())
num = map(int,input().split())
sosu = 0
for i in num :
    hap =0
    if i<=1:
        continue
    for j in range(2,(i/2)+1) :
        if i%j==0 :
            hap+=1
    if hap == 1 :
        sosu +=1
print(sosu)    

""" 
이게 왜 안되는지 모르겠음..


N = int(input())
num = map(int,input().split())

flag = 0
count=0
for i in num :
    if i<=1:
        continue
    for j in range(2,i) :
        if i % j == 0:
            flag=0
        count+=1
            break
        else:
            flag=1
    if flag==1 : 
        print("i:",i)
    flag=0  

print(count) 


"""