Str=input()
lower=0
upper=0
for i in Str:
      if(i.islower()):
            lower+=1
      else:
            upper+=1
if upper>lower:
      print(Str.upper())
else:
      print(Str.lower())