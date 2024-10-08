N = int(input())

fact =2
while(N!=1):
    if(N==0):
        break
    if(N%fact==0):
        print(fact)
        N=N/fact
    else:
        fact+=1

