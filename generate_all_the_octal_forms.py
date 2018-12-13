Array = [-1]*2
#print(len(Array))
#print(Array)
def print_binary(Array, index):
	#Array[index] = 
	#print(index)
	if index > len(Array)-1:
		#print(index)
		print("".join(list(map(str, Array) ) ), end = " " )
		return

	for i in range(8):
		Array[index] = i
		print_binary(Array, index+1)
print_binary(Array, 0)
print()

































'''

#NOTE:  Use FOUR SPACES (Dont USE TABS) for indentation
def main():
	# Your Code Starts Here
	def print_binary(Array, index):
		#Array[index] = 
		#print(index)
		if index > len(Array)-1:
			#print(index)
			print(" ".join(list(map(str, Array) ) ), end = ' ' )
			return

		for i in [0..8]:
			Array[index] = i
			print_binary(Array, index+1)
	testcases = int(input())
	inputs = []
	for i in range(testcases):
		inputs.append(int(input()))
	for i in range(testcases):
		Array = [-1]*i
		print_binary(Array, 0)
if __name__ == "__main__":
	main()
'''