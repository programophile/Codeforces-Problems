for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr.sort()
    if arr[0]<0:
        print(arr[0])
    else:
        print(arr[n-1])