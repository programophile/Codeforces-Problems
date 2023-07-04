import math
for i in range(int(input())):
    n=int(input())
    if n<10:
        print(n)
    else:
            count = 0
            for i in range(1, 10):
                temp = i
                while temp <= n:
                    temp = temp * 10 + i
                    count += 1
            print(count)


