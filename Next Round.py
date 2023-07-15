n,k=map(int,input().split())
list1=[int(i) for i in input().split()]
val=list1[k-1]
count=0
# for i in list1[k]):
#     if int(i)>0:
#         count+=1
#     else:
#         break
for i in range(0,n):
    if list1[i]>=val and list1[i]>0:
        count+=1
    else:
        break
print(count)