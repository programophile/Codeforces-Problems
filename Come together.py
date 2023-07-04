def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    e, f = map(int, input().split())
    x = 0
    y = 0
    if (c - a >= 0 and e - a >= 0) or (c - a <= 0 and e - a <= 0):
        a1 = abs(c - a)
        b1 = abs(e - a)
        x = min(a1, b1)
    if (d - b >= 0 and f - b >= 0) or (d - b <= 0 and f - b <= 0):
        c1 = abs(d - b)
        d1 = abs(f - b)
        y = min(c1, d1)
    print(x + y + 1)


t = int(input())
for _ in range(t):
    solve()