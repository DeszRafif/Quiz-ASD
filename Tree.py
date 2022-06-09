class BinaryTree:
	def __init__(self, data):
		self.data = data  
		self.left = None  
		self.right = None  
	# set data
	def setData(self, data):
		self.data = data
	# get data   
	def getData(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp
	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp
				    

def preorderRecursive(root, result):
    if not root:
        return
    
    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)


def inorderRecursive(root, result):
	if not root:
		return

	inorderRecursive(root.left, result)
	result.append(root.data)
	inorderRecursive(root.right, result)


def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)


def preorderIterative(root, result):
	if not root:
		return
	stack = []
	stack.append(root)
	while stack:
		node = stack.pop()
		result.append(node.data)
		if node.right: stack.append(node.right) #right first - stack pop
		if node.left:  stack.append(node.left)	
		

def inorderIterative(root, result):
	if not root:
		return
	stack = []
	node = root
	while stack or node:
		if node: #node first then stack
			stack.append(node)
			node = node.left   
		else:
			node = stack.pop()
			result.append(node.data)
			node = node.right


def postorderIterative(root, result):
    if not root:
        return
    visited = set() 
    stack = []
    node = root
    while stack or node:
        if node: 
            stack.append(node)
            node = node.left  
        else:
            node = stack.pop()
            if node.right and not node.right in visited:  
                visited.add(node)
                stack.append(node)
                node = node.right 
            else:
                result.append(node.data)
                node = None 


import queue
def levelOrder(root, result):
	if root is None: 
		return
	q = queue.Queue()       
	q.put(root)
	n = None
	while not q.empty():
		n = q.get()  #dequeue FIFO
		#print(n.getData())
		result.append(n.getData())
		if n.left is not None:
			#print("traversing left ..",n.left.getData())
			q.put(n.left)
		if n.right is not None:
			#print("traversing right ..",n.right.getData())
			q.put(n.right)  
