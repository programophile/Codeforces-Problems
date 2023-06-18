import math
for i in range(int(input())):
    n,k=[int(i) for i in input().split()]
    if math.log2(n)<k:
      print(n+1)
    else:
      print(2**k)
