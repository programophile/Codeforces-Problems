
for _ in range(int(input())):
    n=int(input())
    str1=input()
    list1=[n+1]
    temp=n+1

    while n>0:
        if str1[n-1]=="<":
            temp-=1

        else:
            temp+=1
        list1.append(temp)
        n-=1
    print(list1)
    print(len(set(list1)))
