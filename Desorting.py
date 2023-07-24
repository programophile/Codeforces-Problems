import math


def find_difference_array(arr,n):
    res=[]
    for i in range(1,n):
        res.append(abs(arr[i-1]-arr[i]))

    return res
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    a=find_difference_array(arr,n)
    a.sort()
    # print(a)
    if arr!=sorted(arr):
        print(0)
    elif a[0]%2==0:
        print(a[0]//2 +1)
    else:
        print(math.ceil(a[0]/2))