def bubbleSort(lst,x):
    for i in range(x-1):
        for j in range(0, x-i-1):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
lst = [7,6,12,8,5,2,6,2,4,9,10]
x= len(lst)
print (" Before sorting :", lst)
bubbleSort(lst,x)
print (" After sorting :", lst)

