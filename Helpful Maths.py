str1=[int(i) for i in input().split("+")]
str1.sort()
print(*str1, sep="+")