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
import Lexer
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



def SENT(input, tree):
	
	tree1 = DISJ(input)
	if(tree1 != NULL):
		if input[x+1] = IMPOP:
		
			#make the tree1 the left child of IMPOP and call it tree1 
			x=x+2
			tree2 = SENT(input)
			if(tree2 != NULL):
				#make tree2 the right child of tree1
				return tree1

		return tree1
	else return NULL	


def DISJ(input):
	tree1 = CONJ(input)
	if(tree1 !=NULL):
		if input[x+1] = OROP:
			#make the tree1 the left child of ORDOP and call it tree1
			x=x+2
			tree2 = CONJ(input)
			if (tree2 != NULL):
				#make the tree2 the right child of tree1
				return tree1

		return tree1
	else return NULL

def CONJ (input):
	tree1 = LIT(input)
	if(tree1 != NULL):
		if input[x+1] = ANDOP:
			#make node for ANDOP
			#make the tree1 the left child of ANDOP and call it tree 1
			x=x+2
			tree2 = LIT(input)
			if(tree2!=NULL):
				#make the tree 2 the right child of tree 1
				return tree1
		return tree1
	else return NULL

def LIT(input):
	tree1 = ATOM(input)
	if(tree1!=NULL):
		return tree1
	else:
		if input[x] = NEGOP:
			x=x+1
			tree1 = ATOM(input)
			#make tree1 the right child of NEGOP and call it tree 1
			#return tree1
		else return NULL

def ATOM(input):
	if input[x] = VAR:
		tree1 = input[x]
		return tree1
	elif input[x] = LPAREN
		x=x+1
		tree1 = SENT(input)
		if(tree1!=NULL)
			x=x+1
			if input[x] = RPAREN
				return tree1
	elif return NULL 				
	




	
def readFile(inputFile):
	with open(inputFile, 'r') as f:
		data = f.read().replace('\n','')
	return data	



if __name__=='__main__':
	print("hello")
	if len(sys.argv)<2 or len(sys.argv)>2:
		print("incorect number of arguments")
	else:

		formula = readFile(sys.argv[1])		

		parsed = re.split('([v()~&]|->|A[1-9][0-9]*)', formula.replace(" ",""))
		
		parsed = filter(None, parsed)

		for p in parsed:
			print p 
			print("\n")

		print parsed


		x=0
		
#		ASTtree = Node("SENT")
	#	print ASTtree.data
#		ASTtree = SENT(parsed, ASTtree)
	#	print("\n\n\n\n")
	#	print ASTtree.data
	#	ASTtree.traverse(ASTtree)

		
































