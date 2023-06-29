for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%k!=0:
        print(f'1\n{n}')
    else:
        print(2)
        print(1,n-1)
        # temp=1
        # step=2
        # while temp<(n//2):
        #     if temp%k!=0 and n-temp%k!=0:
        #         print(f"{step}\n{temp} {n-temp}")
        #         break
        #     temp+=1
        #     # step+=1