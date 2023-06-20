for i in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    str1=""
    sum=0
    for i in range(len(arr)):
        sum+=abs(arr[i])
        if arr[i]<0:
            str1+=str("a")
        elif arr[i]>0:
            str1+="b"
    count=0

    for i in str1.split("b"):
        if len(i)>0:
            # print("a")
            count+=1
    print(f"{sum} {count}")

