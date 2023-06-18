for i in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    i=0
    max_num=max(arr)
    temp="Yes"
    while i<max_num:
       if arr.count(i)<arr.count(i+1):
           temp="No"
           break
       i+=1
    print(temp)



