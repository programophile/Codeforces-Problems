def replacement(n,arr,str1):
    dict1 = {}
    for i in range(n):
        if arr[i] not in dict1.keys():
            dict1[arr[i]]=[i]
        else:
            dict1[arr[i]].append(i)
    for keys,values in dict1.items():
        val=str1[values[0]]
        for i in values:
            if val!=str1[i]:
                print("No")
                return
    print("Yes")
for _ in range(int(input())):
    n=int(input())
    arr= [int(i) for i in input().split()]

    str1=input()
    replacement(n,arr,str1)

