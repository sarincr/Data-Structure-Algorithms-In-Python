def ShellSort(lst, n):
  h = n // 2
  while h > 0:
    for i in range(h, n):
      t = lst[i]
      j = i
      while j >= h and lst[j - h] > t:
        lst[j] = lst[j - h]
        j -= h
      lst[j] = t
    h = h // 2

lst = [4,9,6,8,5,2,10,7,1,3]
n = len(lst)
print('Array before Sorting:')
print(lst)
ShellSort(lst, n)
print('Array after Sorting:')
print(lst)
