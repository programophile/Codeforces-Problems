for _ in range(int(input())):
    n,digit=map(int,input().split())
    num=input()
    count=0
    for i in num:
        if int(i)<digit:
            idx=num.index(i)
            num=num[:idx]+str(digit)+num[idx:]
            count+=1
            break
    if count==0:
        num=num+str(digit)
    print(num)
