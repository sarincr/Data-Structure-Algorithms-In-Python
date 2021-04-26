def SelSort( lst):
    n = len( lst)
    for i in range( n - 1 ):
        minI = i
        for j in range( i + 1, n ):
            if lst[j] < lst[minI] :
                minI = j
        if minI != i :
            temp = lst[i]
            lst[i] = lst[minI]
            lst[minI] = temp
    return lst


lst = [4,9,6,8,5,2,10,7,1,3]
print("Before Sorted", lst)
print("After Sorted",SelSort(lst))
