import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    ans= math.ceil(n/k)
    if (n-1)%k:
        ans+=1
    print(ans)