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

#from pythonds.basic.stack import Stack
#from pythonds.trees.binaryTree import BinaryTree

class Node:
	def __init__(self, data):
		self.data = data
		self.children = []
	def add_child(self, obj):
		self.children.append(obj)
	def remove_child(parent, child):
		for i in len(parent.children):
			if parent.children[i] == child:
				del parent.children[i]
	def traverse(tree):
		if tree == None: return 0
		for i in len(tree.children):
			print tree.data + traverse(tree.children[i])
		return 0



x = 0 #universal array counter
ASTtree = Node("temp")



def SENT(input, tree):
	
	#put DISJ IMPOP SENT 
	tree.add_child("DISJ")
	tree.add_child("IMPOP")
	tree.add_child("SENT")

	#check DISJ
	#if DISJ true:
		#check IMPOP
		#if IMPOP true
			#check SENT
			#if SENT true
				#return true
			#if SENT false
				#pop off IMPOP and SENT
				#return true
		#else
			#pop off IMPOP and SENT
			#return true
	#else
		#pop DISJ IMPOP SENT off tree
		#return false


def DISJ(input):
	return false
	#put CONJ OROP CONJ on tree
	#check CONJ
	#if CONJ true
		#check ORDOP
		#If ORDOP true
			#Check conj
			#if CONJ true
				#return true
			#if CONJ false
				#pop ORDOP and CONJ off tree
				#return true
		#else
			#pop ORDOP and CONJ off tree
			#return true
	#if false
		#pop off CONJ ORDOP and CONJ
		#return false


def CONJ (input):
	return false
	#put LIT ANDOP LIT on tree
	#Check LIT
	#if LIT true
		#CHECK ANDOP
		#if ANDOP true
			#CHECK LIT
			#if LIT true
				#return true
			#if LIT false
				#pop ANDOP LIT off tree
				#return true
		#if ANDOP false
			#pop ANDOP LIT off tree
			#return true
	#if LIT False
		#pop LIT ANDOP LIT off tree
		#return false



def LIT(input):
	return false
	#Put NEGOP ATOM on tree
	#Check NEGOP
	#if NEGOP true
		#Check Atom
		#if Atom True
			#return true
		#if Atom false
			#pop NEGOP ATOM off tree
			#return false
	#else
		#pop NEGOP ATOM off tree
		#put ATOM on tree
		#Check Atom
		#if ATOM true
			#return truee
		#if Atom False
			#pop Atom off tree
			#return false
	


def ATOM(input):
	return false
	#put LPAREN SENT RPAREN on tree
	#Check LPAREN
	#if LPAREN true
		#Check SENT
		#if SENT true
			#CHECK RPAREN
			#if RPAREN True
				#return true
		#pop LPAREN SENT RPAREN off tree
		#put VAR on tree
		#if VAR true
			#return true
		#else
			#return false
	#Else
		#pop LPAREN SENT RPAREN off tree
		#put VAR on tree
		#Check VAR
		#if VAR true
			#return true
		#else
			#return false

		
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
		
		ASTtree = Node("SENT")
	#	print ASTtree.data
		ASTtree = SENT(parsed, ASTtree)
	#	print("\n\n\n\n")
	#	print ASTtree.data
		ASTtree.traverse(ASTtree)

		
































