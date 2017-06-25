#http://www.spoj.com/problems/CPTTRN3/
from __future__ import print_function
def printingFunction(l,c):
	rowCount = l*2 + l+1
	columnCount = c*2 + c+1
	for i in range(0,rowCount):
		for j in range(0,columnCount):
			if (i == (rowCount-1) or j == (columnCount-1) or (j%3 == 0) or (i%3 == 0)):
				print('*', sep='', end='')
			else:
				print('.', sep='', end='')
		print('\n')

t=input()
for i in range(0,t):
	l,c = map(int, raw_input().split())
	printingFunction(l,c)
print('\n')
