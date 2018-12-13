class Stack:
	def __init__(self):
		self.items = []

	def insert(self, node):
		self.items.append(node)

	def pop (self):
		self.items.pop(0)

	def Maxim(self):
		return max(self.items)

	def Minm(self):
		return min(self.items)

	def print_stack(self):
		print(self.items)


s = Stack()

s.insert(30)
s.insert(20)
s.insert(40)
s.insert(50)
s.insert(60)
s.print_stack()
s.pop()
s.print_stack()
print(s.Maxim(), end=" ")


