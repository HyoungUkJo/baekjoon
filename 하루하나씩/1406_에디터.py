str = input()
arr = list(str)
max = len(arr)
pointer = max

N = int(input())


for _ in range(N) :
    option = input().split(" ")
    option = list(option)
    # print("option:",option[0],"pointer:",pointer,"max:",max,"arr:",arr)

    if option[0] == 'L':
        if pointer==0:
            continue
        pointer -=1
        
    elif option[0] == 'D':    
        if pointer == max+1:
            continue
        pointer +=1

    elif option[0] == 'B':
        if pointer ==0:
            continue
        temp_arr = arr[pointer:len(arr)]
        # print("temp",temp_arr)
        # print("slice:",arr[0:pointer-1])
        arr = arr[0:pointer-1]+temp_arr
        max -=1
        pointer-=1

    elif option[0] == 'P':
        arr.insert(pointer,option[1])
        max +=1
        pointer+=1

    else :
        break

print(*arr,sep="")