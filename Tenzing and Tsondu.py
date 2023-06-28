for _ in range(int(input())):
    n=input()
    ts=[int(i) for i in input().split()]
    ten=[int(i) for i in input().split()]
    # print(ts,ten)
    if sum(ts)>sum(ten):
        print("Tsondu")
    elif sum(ts)<sum(ten):
        print("Tenzing")
    else:
        print("Draw")