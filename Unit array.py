import math
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    sum=0
    mul=1
    operation=0
    for i in arr:
        sum+=i
        mul*=i
    if sum<0:
        operation = math.ceil(abs(sum)/2)
        if operation%2==0:
            if mul<0:
                operation+=1

        else:
            if mul>0:
                operation+=1
    elif sum>=0:
        if mul>0:
            operation=0
        else:
            operation=1
    print(operation)
    # if mul>0 and sum>-1:
    #     print()

    # sum_arr=sum(arr)
    # mul_arr= [-1,-1,-1,1,1]