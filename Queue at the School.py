n,t=map(int,input().split())
str1=input()
list1=[0]*n
for i in range(n):
    list1[i]=str1[i]
    # if str1[i]=='B':
    #     if str1[i+1]=="G":
    #         list1[i+t]=1

for i in range(t):
    temp=0
    while temp<n-1:
        if list1[temp]=="B" and list1[temp+1]=="G":
            list1[temp],list1[temp+1]=list1[temp+1],list1[temp]
            temp+=1
        temp+=1
for i in list1:
    print(i,end="")
