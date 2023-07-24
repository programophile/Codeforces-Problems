import math

l,b=map(int,input().split())
if l==b:
    print(1)
else:
    count=0
    while True:
        if l*3>b*2:
            print(count+1)
            break
        else:
           l=l*3
           b=b*2
           count+=1
    # for i in range(3,1000,3):
    #     if i*l>b*i-1:
    #         print(i//2)
    #         break
    #     else:
    #         l=i+l
    #         b=(i-1)*b