def particles(arr,n):
    new_arr=[0,0]
    if all([val < 0 for val in arr]):
        print(max(arr))
        return
    for i in range(n):
        if arr[i]>0:
            if i%2==0:
                new_arr[0]+=arr[i]
            else:
                new_arr[1]+=arr[i]
    print(max(new_arr))

for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    particles(arr,n)






