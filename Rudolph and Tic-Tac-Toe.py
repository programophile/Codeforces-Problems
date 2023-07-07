def chkList(lst):
    if len(lst) < 0:
        res = True
    res = lst.count(lst[0]) == len(lst)

    if (res):
        return True
    else:
        return False
def mat_arr():
    arr=[[0,0,0],[0,0,0],[0,0,0]]
    list1=[]
    for i in range(3):
        input1=input()
        arr[i][0],arr[i][1],arr[i][2]=input1[0],input1[1],input1[2]
    for i in range(3):
        if arr[i][0]==arr[i][1]==arr[i][2]:
            if arr[i][0]!=".":
                list1.append(arr[i][0])
        elif arr[0][i]==arr[1][i]==arr[2][i]:
            if arr[0][i]!=".":
                list1.append(arr[0][i])
    if arr[0][0]==arr[1][1]==arr[2][2]:
        if arr[0][0] != ".":
            list1.append(arr[0][0])
    elif  arr[0][2]==arr[1][1]==arr[2][0]:
        if arr[0][2] != ".":
            list1.append(arr[0][2])
        # print(list1)

    if len(list1)==0:
        print("DRAW")
    elif chkList(list1)==True:
        print(list1[0])
    else:
        print("DRAW")
for _ in range(int(input())):
    mat_arr()