str1=input()
arr=[]
count=0
for i in str1:
    if i not in arr:
        count+=1
        arr.append(i)
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")