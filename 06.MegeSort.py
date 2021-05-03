def merge(x, l, m, r):
	left = m - l + 1
	right = r- m
	LeftPart = [0] * (left)
	RightPart = [0] * (right)
	for i in range(0 , left):
		LeftPart[i] = x[l + i]

	for j in range(0 , right):
		RightPart[j] = x[m + 1 + j]
	i = 0	  
	j = 0	  
	k = l	 
	while i < left and j < right :
		if LeftPart[i] <= RightPart[j]:
			x[k] = LeftPart[i]
			i += 1
		else:
			x[k] = RightPart[j]
			j += 1
		k += 1
	while i < left:
		x[k] = LeftPart[i]
		i += 1
		k += 1
	while j < right:
		x[k] = RightPart[j]
		j += 1
		k += 1
def mergeSort(x,l,r):
	if l < r:
		m = (l+(r-1))//2
		mergeSort(x, l, m)
		mergeSort(x, m+1, r)
		merge(x, l, m, r)

x = [9,5,6,3,4,8,2,1,10]
n = len(x)
print ("Array  = ")
for i in range(n):
	print ("%d" %x[i]),
mergeSort(x,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
	print ("%d" %x[i]),
