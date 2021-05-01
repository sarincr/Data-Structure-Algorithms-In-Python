def heap(x, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and x[largest] < x[l]:
        largest = l
    if r < n and x[largest] < x[r]:
        largest = r
    if largest != i:
        x[i], x[largest] = x[largest], x[i]
        heap(x, n, largest)


def devide(x):
    n = len(x)
    for i in range(n//2 - 1, -1, -1):
        heap(x, n, i)
    for i in range(n-1, 0, -1):
        x[i], x[0] = x[0], x[i]
        heap(x, i, 0)


lst = [4,9,6,8,5,2,10,7,1,3]
print("Array = ", lst)
devide(lst)
n = len(lst)
print("Sorted Array = ", lst)

