def duplicates_array(n):
	empty_e = {}
	for i in range(0, len(n)-1):
		if n[i] not in empty_e:
			empty_e[n[i]] = "count"
	print(empty_e)

#duplicates_array([1, 2, 3, 3, 3, 4])
arra = []
def duplicates_array(n, index, array):
	#print(n[index])	
	value = n[index]	
	#print(value)
	#print(n[:index]+n[index+1:])
	#print(index)
	if not value in n[:index]+n[index+1:] :
		#print(n[index])
		array.append(n[index])		
		#print(arra)
		#pass
	if index == 0:
		#print(array)
		return
	duplicates_array(n[:index]+n[index+1:], index-1, array)


n = [2, 2, 3, 4, 5, 6, 5]
#duplicates_array(n, len(n)-1, arra)
#arra.reverse()
#print(arra)
#print(len(n)-1)
'''
print(n[:0]+n[1:])
print(n[:1]+n[2:])
print(n[:2]+n[3:])
print(n[:3]+n[4:])
print(n[:4]+n[5:])

# Complete the function below.
def removeDuplicates(a):
	arra = []
	def duplicates_array(n, index, array):
		value = n[index]
		if not value in n[:index]+n[index+1:] :
			array.append(n[index])
		if index == 0:
			duplicates_array(n[:index]+n[index+1:], index-1, array)
			
	return arra
'''


#reversed.arra
'''
a = [2, 2, 2]
for i, element in enumerate(a):	
	if element in a[:i]+a[i+1:] :
		a[i] = -1
for i, element in enumerate(a):
	if i == -1:
		del a[i]
print(a)
'''
# Complete the function below.
#def removeDuplicates(a):
def removeDuplicates_helper(arr, n):
	if n==0 or n==1:
		return n
	j = 0
	for i in range(0, n-1):
		if arr[i] != arr[i+1]:
			arr[j] = arr[i]
			j +=1
	arr[j] = arr[n-1]
	return j

a = [1, 2, 2, 3, 4, 4, 4, 5, 5]

n = removeDuplicates_helper(a, len(a))

a = a[:n]
print(a)
for i in range(0, n): 
	print (" %d "%(a[i]), end = " ")
