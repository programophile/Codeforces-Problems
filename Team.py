ans=0
for _ in range(int(input())):
    arr=[int(i) for i in input().split()]
    sum1=sum(arr)

    if sum1>1:
        ans+=1
print(ans)
