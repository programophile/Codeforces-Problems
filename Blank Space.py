for i in range(int(input())):
    n=int(input())
    str1=input().split(" ")
    count=0
    temp=0
    for j in range(n):
        # if j!=n-1:
            if str1[j]=="0" and j!=n-1:
                temp+=1
            elif str1[j]=="0" and j==n-1:
                temp+=1
                if temp>count:
                    count=temp
            else :
                if count<temp:
                    count=temp
                temp=0
    print(count)


