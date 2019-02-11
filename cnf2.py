import ast
import argparse as ap
import operator
from collections import Counter
import fileinput
import sys
import csv
import re
from StringIO import StringIO
import tokenize
from Lexer import *
from ourTree import *

#from pythonds.basic.stack import Stack
#from pythonds.trees.binaryTree import BinaryTree

class Node:
	def __init__(self, data):
		self.l = None
		self.r = None
		self.v = val
class Tree:
	def __init__(self):
		self.root = None
	

x = 0 #universal array counter
#lx = Lexer(rules)



ops = [
	('~', 'NEGOP'),
	('&', 'ANDOP'),
	('v', 'OROP'),
	('->', 'IMPOP'),
	('\(', 'LPAREN'),
	('\)', 'RPAREN'),
	('A[1-9][0-9]*', 'VAR')
] 

lx = Lexer(ops)





def SENT(array):
	global x	
	tree1 = DISJ(array)
	if(tree1 is not None):
		if(x+1>=len(array)):
			return tree1
		
		lx.input(array[x+1])
		temp = str(lx.nextToken())
		if temp=="IMPOP":		
						
			#make the tree1 the left child of IMPOP and call it tree1 
			
			node = TreeNode("IMPOP","->")			
			node.left = tree1
			


			if(x+2>=len(array)):
				return None
			x=x+2
			tree2 = SENT(array)
			if(tree2 is not None):
				#make tree2 the right child of tree1
				node.right = tree2
				return node

		return tree1
	else:
		return None	


def DISJ(array):
	global x
	tree1 = CONJ(array)
	if(tree1 is not None):
		if (x+1>=len(array)):
			return tree1
		lx.input(array[x+1])
		temp = str(lx.nextToken())
		if temp == "OROP":
			
			#make the tree1 the left child of ORDOP and call it tree1
			node = TreeNode("OROP","v")
			node.left = tree1
		
			if(x+2>=len(array)):
				return None

			x=x+2
			tree2 = CONJ(array)
			if(tree2 is not None):

				#make the tree2 the right child of tree1
				node.right = tree2
				return node

		return tree1
	else:
		return None

def CONJ (array):
	global x
	tree1 = LIT(array)
	if(tree1 is not None):
		if(x+1>=len(array)):
			return tree1
		lx.input(array[x+1])
		temp=str(lx.nextToken())
		if temp== "ANDOP":
			#make node for ANDOP
			#make the tree1 the left child of ANDOP and call it tree 1
			node = TreeNode("ANDOP","&")
			node.left = tree1

			if(x+2>=len(array)):
				return None
			x=x+2
			tree2 = LIT(array)
			if(tree2 is not None):
				#make the tree 2 the right child of tree 1
				node.right = tree2
				return node
		return tree1
	else:
		 return None

def LIT(array):
	global x
	tree1 = ATOM(array)
	if(tree1 is not None):
		return tree1
	else:
		lx.input(array[x+1])
		temp=str(lx.nextToken())
		if temp== "NEGOP":
			if(x+1>=len(array)):
				return None
			x=x+1
			tree1 = ATOM(array)
			#make tree1 the right child of NEGOP and call it tree 1
			#return tree1
			node = TreeNode("NEGOP","~")
			node.right = tree1
			return node
		else:
			 return None

def ATOM(array):
	global x
	lx.input(array[x])
	temp = str(lx.nextToken())
	if temp== "VAR":
#		tree1 = array[x]
		tree1 = TreeNode("VAR",array[x])
		return tree1
	lx.input(array[x])
	temp = str(lx.nextToken())
	if (temp == "LPAREN"):
		if(x+1>=len(array)):
			return None
		x=x+1
		tree1 = SENT(array)
		if(tree1 is not None):
			if(x+1>=len(array)):
				return None
			x=x+1
			lx.input(array[x])
			temp = str(lx.nextToken())
			if temp == "RPAREN":
				return tree1
	else:
		 return None			
	




	
def readFile(inputFile):
	with open(inputFile, 'r') as f:
		data = f.read().replace('\n','')
	return data	



if __name__=='__main__':

#	print("hello")
	if len(sys.argv)<2 or len(sys.argv)>2:
		print("incorect number of arguments")
	else:

		formula = readFile(sys.argv[1])		

		parsed = re.split('([v()~&]|->|A[1-9][0-9]*)', formula.replace(" ",""))
		
		parsed = filter(None, parsed)

	#	for p in parsed:
	#		print p 
	#		print("\n")

	#	print parsed


		#x=0
		
				
	#	node = TreeNode("IMPOP", "->")
	#	print node.val
		
		tree = SENT(parsed)
	#	print(tree.val)		
	#	print(tree.left.val)

		print("AST pre-order traversal tree\n")
		
		tree.inorderTraversal()	



#		inorderTraversal(tree)

		


#		ASTtree = Node("SENT")
	#	print ASTtree.data
#		ASTtree = SENT(parsed, ASTtree)
	#	print("\n\n\n\n")
	#	print ASTtree.data
	#	ASTtree.traverse(ASTtree)

		
































