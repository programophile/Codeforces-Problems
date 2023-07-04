# def printing(l=0):
#     n,k,x=map(int,input().split())
#     # if n%k==0 and k!=1:
#     #     print("Yes")
#     #     print(n//k)
#     #     for i in range(n//k):
#     #         print(k,end=" ")
#     #     print()
#     #     return
#         # print(str(k)+" "*(n//k))
#     for i in range(1,k+1):
#         if i!=x:
#             if n%i==0:
#                 print("Yes")
#                 print(n//i)
#                 for _ in range(n//i):
#                     print(i,end=" ")
#                 print()
#                 return
#     print("No")
# for _ in range(int(input())):
#     printing()
#
#     # elif x!=1:
#     #     print("Yes")
#     #     print(n)
#     #     for i in range(n):
#     #         print(1,end=" ")
#     # elif k>2 and n%2==0:
#     #     print("Yes")
#     #     print(n//2)
#     #     for i in range(n//2):
#     #         print(2,end=" ")
#     # else:
#     #     print("No")
def solve():
    n, k, x = map(int, input().split())
    if k == 1 and x == 1:
        print("NO")
        return
    if n % 2 != 0:
        if k < 3 and x == 1:
            print("NO")
            return
    print("YES")
    if x != 1:
        print(n)
        for i in range(1, n+1):
            print("1", end=" ")
        print()
        return
    if n % 2 == 0:
        print(n // 2)
        for i in range(n // 2):
            print("2", end=" ")
        print()
    else:
        a = n - 3
        b = a // 2
        print(1 + b)
        for i in range(b):
            print("2", end=" ")
        print("3")


t = int(input())
for _ in range(t):
    solve()