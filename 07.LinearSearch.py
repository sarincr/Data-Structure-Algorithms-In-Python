def linear_search(x):
  lst = [6,4,8,2,9,4,54,3,22]
  print("List  = ", lst)
  index = 0
  state = False
  while index < len(lst) and state == False:
    if lst[index] == x:
      state = True
    else:
      index = index + 1
  return state

print(linear_search(54))
