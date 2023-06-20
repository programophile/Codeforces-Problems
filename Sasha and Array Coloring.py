# def color_arr(a)
for i in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    cost=0
    while len(arr)>1:
        cost+=max(arr)-min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))

    print(cost)
