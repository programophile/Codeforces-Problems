
for i in range(int(input())):
    n=int(input())
    sum=n

    while n>0:
        # if n%2==0:
            sum=sum+(n//2)
            n=n//2
        # else:
        #     sum+= math.ceil((n/2)-1)
        #     n=math.ceil((n/2)-1)
    print(sum)