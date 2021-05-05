def partition(x, left, right):
  i = left - 1
  point = x[right]
  for j in range(left, right):
    if x[j] < point:
      i += 1
      x[i], x[j] = x[j], x[i]
  x[i + 1], x[right] = x[right], x[i + 1]
  return i + 1
def quicksort(lst, left, right):
    if left < right:
      pi = partition(lst, left, right)
      quicksort(lst, left, pi - 1)
      quicksort(lst, pi + 1, right)


if __name__ == "__main__":
  lst = [7,6,9,1,10,3,2,5,8,4]
  print("Array =: " + str(lst))
  quicksort(lst, 0, len(lst) - 1)
  print("Sorted Array = : " + str(lst))