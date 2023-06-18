for _ in range(int(input())):
    n=int(input())
    print(*(n+1 - int(a) for a in input().split()),sep=" ")