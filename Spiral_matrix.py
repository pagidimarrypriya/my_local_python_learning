'''
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def spiral_print(a, ROW, COLUMN, MAX_ROW, MAX_COLUMN):
	if ROW == COLUMN:
		print(a[ROW][COLUMN])
		return
	for j in range(COLUMN, MAX_COLUMN):
		print(a[ROW][j])
	for i in range(MAX_ROW, ROW, -1):
		print(a[i][MAX_COLUMN])
	for j in range(MAX_COLUMN, COLUMN, -1):
		print(a[MAX_ROW][j])
	for i in range(ROW, MAX_ROW):
		print(a[i][COLUMN])

	spiral_print(a, ROW+1, COLUMN+1, MAX_ROW-1, MAX_COLUMN-1)
'''




def print_top_bottom_elements(a, r, c, R, C, order):
	if order != 'reverse':
		for j in range(c, C):
			print(a[r][j], end=" ")
	else:
		for j in range(C, c, -1):
			print(a[R][j], end=" ")
	return
def print_left_right_elements(a, r, c, R, C, order):
	if order != 'reverse':
		for i in range(r, R):
			print(a[i][C], end=" ")
	else:
		for i in range(R, r, -1):
			print(a[i][c], end=" ")


#a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
def actual_metrix(a, r, c, R, C):
	#if r > R and c > C and r == c:
	#	print(a[r][c], end=" ")
	#	return
	if r-R > 0 or c-C > 0 :
		if (len(a)-1)%2 == 0 and (len(a[0])-1)%2 == 0:
			print(a[(len(a)-1)//2][(len(a[0])-1)//2])
			#return
		return
	
	print_top_bottom_elements(a, r, c, R, C, "proper")

	print_left_right_elements(a, r, c, R, C, "proper")

	print_top_bottom_elements(a, r, c, R, C, "reverse")

	print_left_right_elements(a, r, c, R, C, "reverse")

	actual_metrix(a, r+1, c+1, R-1, C-1)

#actual_metrix(a, 0, 0, len(a)-1, len(a[0])-1 )

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

newone = []#[[0]*2] * 2
count = 0
c = 3
r = 3
for i in range(r):
	#print(i)
	newone.append([a[j] for j in range(count, count+c) ])
	count = count + c
	#c = c + c


print(newone)




#print(a[(len(a)-1)//2][(len(a[0])-1)//2])
#print((len(a)-1)//2)
#print((len(a[0])-1)//2)
			
			
			

#matrix = []
def print_top_bottom_elements(a, r, c, R, C, order):
	if order != 'reverse':
		for j in range(c, C):
			print(a[r][j], end=" ")
	else:
		for j in range(C, c, -1):
			print(a[R][j], end=" ")
	return
def print_left_right_elements(a, r, c, R, C, order):
	if order != 'reverse':
		for i in range(r, R):
			print(a[i][C], end=" ")
	else:
		for i in range(R, r, -1):
			print(a[i][c], end=" ")

def actual_metrix(a, r, c, R, C):
	#if r > R and c > C and r == c:
	#	print(a[r][c], end=" ")
	#	return
	if r-R > 0 or c-C > 0 :
		if (len(a)-1)%2 == 0 and (len(a[0])-1)%2 == 0:
			print(a[(len(a)-1)//2][(len(a[0])-1)//2])
			#return
		return
	
	print_top_bottom_elements(a, r, c, R, C, "proper")

	print_left_right_elements(a, r, c, R, C, "proper")

	print_top_bottom_elements(a, r, c, R, C, "reverse")

	print_left_right_elements(a, r, c, R, C, "reverse")

	actual_metrix(a, r+1, c+1, R-1, C-1)

def return_matrix(lists, r, c):
	metrix = []
	count = 0
	for i in range(r):
		metrix.append( [lists[j] for j in range(count, count+c)])
		count = count+c
	return metrix

testcase = int(input())
lists = []
a = []
for i in range(testcase * 2 - 1):
	r, c = map(int, input().split(" "))
	#print(r, c)
	lists =  list ( map(int, input().split(" ") ) )
	a = list ( return_matrix(lists, r, c) )
	actual_metrix(a, 0, 0, len(a)-1, len(a[0])-1 )








