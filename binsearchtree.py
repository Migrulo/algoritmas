#!/usr/bin/python
import sys

class node:
	def __init__(self, parent):
		self.key = None
		self.parent = parent
		self.left = None
		self.right = None

def minn(bst):
	if bst.left == None:
		return bst
	else:
		return minn(bst.left)

def nextt(bst):
	if bst.right != None:
		return minn(bst.right)
	else:
		while 1:
			if bst == None:
				return None
			parent = bst.parent
			if parent == None:
				return None
			if parent.left == bst:
				return parent
			else:
				bst = parent

def add(bst, toadd):
	if bst.key == None:
		bst.key = toadd
		print "-",
		return bst
	elif bst.key > toadd:
		if bst.left == None:
			bst.left = node(bst)
		return add(bst.left, toadd)
	elif bst.key < toadd:
		if bst.right == None:
			bst.right = node(bst)
		return add(bst.right, toadd)
	else:
		print "+",
		return bst



inp = []
for line in sys.stdin:
    inp.append(line)
del inp[0]

bst = node(None)
for i in inp:
	added = add(bst, int(i))
	x = nextt(added)
	if x:
		print x.key
	else:
		print "-"

