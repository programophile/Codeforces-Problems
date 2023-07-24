ans=0
for i in range(1,6):
    list1=[int (i) for i in input().split()]
    if 1 in list1:
        ans=abs(3-i)
        ans+=abs(3-list1.index(1)-1)
print(ans)