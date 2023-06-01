def all_even(lst):
    if all(number % 2 == 0 for number in lst):
        return True
    return False
test_cases=int(input())
for i in range(test_cases):
    arr_length=int(input())
    arr=input().split(" ")
    arr=[int(i) for i in arr]
    if min(arr)%2==1:
        print("YES")
    else:
        if all_even(arr):
            print("YES")
        else:
            print("NO")



