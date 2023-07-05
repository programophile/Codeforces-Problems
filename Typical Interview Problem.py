
def inr(n,str1):
    str2="FBFFBFFBFBFFBFFB"
    if n<=8:
        if str1 in str2:
            print('Yes')
            return
    else:
        str2=str2*(n-8)
        if str1 in str2:
            print("Yes")
            return
    print("NO")

    # f_count=0
    # b_count=0
    # for i in range(n):
    #     if str1[i]=="B" :
    #         b_count+=1
    #         f_count=0
    #     elif str1[i]=="F":
    #         f_count+=1
    #         b_count=0
    #     if f_count>2 or b_count>1:
    #         print("No")
    #         return
    # print("YES")
for _ in range(int(input())):
    n = int(input())
    str1 = input()
    inr(n,str1)