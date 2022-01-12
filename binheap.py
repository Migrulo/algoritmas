#!/usr/bin/python
import sys

def swap(arr, ind1, ind2):
	temp = arr[ind1]
	arr[ind1] = arr[ind2]
	arr[ind2] = temp

def heap_stiff_up(heap, ind):
	if ind <= 0:
		return
	if heap[ind] > heap[(ind - 1) / 2]:
		swap(heap, (ind - 1) / 2, ind)
		heap_stiff_up(heap, (ind - 1) / 2)
	return

def heap_stiff_down(heap,ind):
	if (ind * 2 + 2) > len(heap) - 1:
		return
	if heap[ind * 2 + 2] > heap[ind * 2 + 1]:
		maxx = 2
	else:
		maxx = 1
	if heap[ind] < heap[ind * 2 + maxx]:
		swap(heap, ind, ind * 2 + maxx)
		heap_stiff_down(heap, ind * 2 + maxx)
	return

def heap_add(heap, toadd):
	heap.append(toadd)
	heap_stiff_up(heap, len(heap) - 1)

def heap_remove(heap):
	remove = heap[0]
	heap[0] = heap[-1]
	del heap[-1]
	heap_stiff_down(heap, 0)
	return remove
			
		
heap = []
#f = open("4.in", 'r')
inp = []
for line in sys.stdin:
	inp.append(line)
del inp[0]

for i in inp:
	if i == "GET\n":
		r = heap_remove(heap)
		print r
	else:
		heap_add(heap, int(i))
		