def main(n,m,k,x,y):

    # for _ in range(t):

        can_escape = True
        for i in range(k):
            xi, yi = map(int, input().split())
            dx = abs(x - xi)
            dy = abs(y - yi)
            if (dx + dy) % 2 == 0:
                can_escape=False
        if can_escape==False:
            print("NO")
            return
        print("Yes")

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    x, y = map(int, input().split())
    main(n,m,k,x,y)