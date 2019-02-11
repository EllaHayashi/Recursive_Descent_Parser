class TreeNode:
	def __init__(self, key, val, left = None, right = None, parent = None):
		self.key = key
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent

	def hasLeftChild(self):
		return self.left

	def hasRightChild(self):
		return self.right

	def isLeftChild(self):
		return self.parent and self.parent.left == self

	def isRightChild(self):
		return self.parent and self.parent.right == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.right or self.left)

	def hasAnyChildren(self):
		return self.right or self.left

	def hasBothChildren(self):
		return self.right and self.left

	def replaceNodeData(self, key, value, lc, rc):
		self.key = key
		self.val = value
		self.left = lc
		self.right = rc
		if self.hasLeftChild():
			self.left.parent = self
		if self.hasRightChild():
			self.right.parent = self

	def inorderTraversal(self):
		print self.val
		if(self.left is not None):
			self.left.inorderTraversal()
		if(self.right is not None):
			self.right.inorderTraversal()






