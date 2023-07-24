def check(list):
    return len(set(list)) == 1


for _ in range(int(input())):
    n,k=map(int,input().split())
    list1=[int(i) for i in input().split()]
    count=0
    for i in range(n//2):
        if list1[i]!=list1[n-1-i]:
            count+=1
    if n%2!=0 :
        if n>3:
            if  list1[n//2]==list1[n//2 -1]==list1[n//2 +1]:
                count+=1
    elif n%2==0:
        count-=1
    if check(list1):
        print(0)
    else:
        print(count)