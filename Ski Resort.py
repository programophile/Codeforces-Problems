import math
def nCr(n, r):
    return (math.factorial(n) / (math.factorial(r)*math.factorial(n-r)))
for _ in range(int(input())):
    n,k,q=map(int,input().split())
    arr=[int(i) for i in input().split()]
    temp1=0
    temp2=0
    count=0
    new_arr=[0]*n
    pointer=0
    for i in range(n):
        if arr[i]<=q:
            new_arr[pointer]+=1
        else:
            pointer+=1
    # print(new_arr)
    for j in new_arr:
        if j>=k:
            for f in range(1,j-k+2):
              # print(f)
              count+=f
    print(count)