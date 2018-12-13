import queue
class Node():	
	def __init__(self, data): 
		self.data = data  
		self.left = None  
		self.right = None


def insert(root, node):
	if root is None:
		root = node

	if root.data > node.data:
		if root.left is None:
			root.left = node
		else:
			insert(root.left, node)
	elif root.data < node.data:
		if root.right is None:
			root.right = node
		else:
			insert(root.right, node)
def pre_order(root):
	if root is None:
		return
	print(root.data, end=" ")
	if root.left is not None:
		pre_order(root.left)
	if root.right is not None:
		pre_order(root.right)

def post_order(root):
	if root is None:
		return
	#print(root.data, end=" ")
	if root.left is not None:
		post_order(root.left)
	if root.right is not None:
		post_order(root.right)
	print(root.data, end=" ")

def in_order(root):
	if root is None:
		return
	if root.left is not None:
		in_order(root.left)
	print(root.data, end=" ")
	if root.right is not None:
		in_order(root.right)


def search_node(root, data):
	if root is None:
		print("False")
		return False
	#print(root.data, "root_data")
	if root.data == data:
		print("True")
		return True
	elif root.data < data:
		#print(root.data, data, "right")
		search_node(root.right, data)
	elif root.data > data:
		#print(root.data, data, "left")
		search_node(root.left, data)

def level_order(root):
	if root is None:
		return
	L = queue.Queue()
	L.put(root)
	#print(L.empty())
	while not L.empty() :
		root = L.get()
		print(root.data, end=" ")
		if root.left is not None:
			L.put(root.left)			
		if root.right is not None:
			L.put(root.right)

		
	#print(root.data, end=" ")
	if root.left is not None:
		level_order(root.left)
	elif root.right is not None:
		level_order(root.right)


def delete_node(root, data):
	if root is None:
		return




r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

in_order(r)
print("\n")
pre_order(r)
print("\n")
post_order(r)
print("\n")
level_order(r)

#search_node(r, 30)
#search_node(r, 90)
#search_node(r, 10)
#search_node(r, 80)