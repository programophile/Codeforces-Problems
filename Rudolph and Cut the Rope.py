for _ in range(int(input())):
    count=0
    for _ in range (int(input())):
        a,b=map(int,input().split())
        if a>b:
            count+=1
    print(count)