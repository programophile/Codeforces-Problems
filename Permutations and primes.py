# def mex(arr):
#     # Sort the array
#     arr.sort()
#
#     mex = 1
#     if arr[0]>2:
#         mex=arr[0]-1
#     elif arr[0]==1:
#         for i in arr:
#             if mex==i:
#                 mex+=1
#     # return mex as answer
#     return mex
# def find_prime(num):
#     flag=False
#     if num == 1:
#         return False
#
#     elif num > 1:
#
#     # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#                 # if factor is found, set flag to True
#                 # flag = True
#                 return False
#                 # flag = True
#                 # # break out of loop
#                 # break
#
#         # check if flag is True
#         return True
# for _ in range(int(input())):
#     arr=[]
#     n=int(input())
#     for i in range(1,n):
#         # print(mex([i,i+1]))
#         if  find_prime(mex([i,i+1]))==True:
#             arr.append(i)
#             arr.append(i+1)
#     if n==1:
#         arr.append(1)
#     a=[*set(arr)]
#     for i in a:
#         print(i,end=" ")
#     print()
# #find_prime(mex([i,i]))==True and

for _ in range(int(input())):
    n = int(input())
    a = [0] * n
    a[0] = 2
    a[n - 1] = 3
    a[n // 2] = 1
    counter = 4
    for i in range(1, n - 1):
        if i == n // 2:
            continue
        a[i] = counter
        counter += 1
    print(*a)