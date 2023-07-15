for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[int(i) for i in input().split()]
    list1=[]
    for i in range(n-1):
        list1.append(abs(arr[i]-arr[i+1]))
    list1.sort()
    # print(list1)
    print(sum(list1[:n-k]))