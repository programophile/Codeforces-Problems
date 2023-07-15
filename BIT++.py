x=0
for _ in range(int(input())):
    str1=input()
    x+=(str1.count("+")//2)
    x-=(str1.count("-")//2)
print(x)