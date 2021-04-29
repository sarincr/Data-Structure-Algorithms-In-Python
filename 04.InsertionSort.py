def InsSort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i-1
        while j >= 0 and x < lst[j] :
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = x
    return(lst)

lst = [4,9,6,8,5,2,10,7,1,3]
print("Before Sorted", lst)
print("After Sorted",InsSort(lst))
