
# def splitter(n,m):
#
#     if n==m:
#         return True
#     elif n%3!=0:
#         return False
#     if list1[n]!=None:
#         return list1[n]
#     # if list1[n//3]!=None:
#     #     return list1[n//3]
#     # if list1[(2*n)//3]!=None:
#     #     return list1[(2)]
#     list1[n // 3] = splitter(n // 3, m)
#     list1[(2 * n) // 3] = splitter((2 * n) // 3, m)
#     return list1[n//3] or list1[(2*n)//3]


def splitter(n,m):
    while n>=m:
        if n==m:
            # print("yeeees")
            return True
        elif n%3!=0:
            # print("nnnn")
            return False
        n//=3
        if (n&-n)<(m&-m):
            n*=2
# roll=int(input())
# for ink in range(roll):
#   n,m=map(int,input().split())
#   r=0
#   for a in range(15):
#     for b in range(15):
#       if 3**b*m==2**a*n:
#         if a<=b:
#           r+=1
#   if r>0:
#     print('Yes')
#   else:
#     print('No')
for _ in range(int(input())):
    n,m=map(int,input().split())
    if splitter(n,m):
        print("Yes")
    else:
        print("No")
