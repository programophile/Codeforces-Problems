for _ in range(int(input())):
    arr=[int(i) for i in input().split()]
    arr.sort()
    if arr[2]+arr[1]>=10:
        print("YES")
    else:
        print("NO")