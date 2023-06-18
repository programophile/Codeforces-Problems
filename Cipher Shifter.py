for i in range(int(input())):
    n=int(input())
    str1=input()
    temp=0
    while temp<n:
        print(str1[temp],end="")
        temp=str1.index(str1[temp],temp+1,n)
        temp+=1
    print()

