def gap_sort(x):
    gap = len(x)
    swap= True
    while gap > 1 or swap:
        gap = max(1, int(gap / 1.3))  
        swap= False
        for i in range(len(x) - gap):
            j = i+gap
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
                swap= True
 
lst = [3,6,4,8,9,0,6,5,2,10,1]
print("Unsorted: ", lst)
gap_sort(lst)
print("Sorted:  ", lst)
