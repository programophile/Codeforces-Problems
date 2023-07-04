for _ in range(int(input())):
    str1=input()

    if len(str1)>10:
        print(f"{str1[0]}{len(str1)-2}{str1[-1]}")
    else:
        print(str1)