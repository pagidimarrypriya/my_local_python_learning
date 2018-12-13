phone_numbers = {2: 'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
#print(len(Array))
#print(Array)
def print_phone(Array, index):
	#Array[index] = 
	#print(index)
	if index > len(Array)-1:
		#print(index)
		print("".join(list(map(str, Array) ) ), end = " " )
		return
	for i in string:		
		Array[index] = i
		print_phone(Array, index+1)
string = ''
given = 89
for i in str(given):
	string += phone_numbers[int(i)]
Array = [-1]*len(str(given))

print_phone(Array, 0)
print()

