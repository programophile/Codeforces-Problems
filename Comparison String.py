
for _ in range(int(input())):
    n=int(input())
    str1=input()
    # list1=[n+1]
    temp=1
    ans=1
    for i in range(n-1):

        if str1[i]==str1[i+1]:
            temp+=1

        else:
            ans = max(temp+1, ans)

            temp=1
    ans = max(temp+1, ans)


    print(ans)
    # while n>0:
    #     if str1[n-1]=="<":
    #         temp-=1
    #
    #     else:
    #         temp+=1
    #     list1.append(temp)
    #     n-=1
    # print(list1)
    # print(len(set(list1)))
