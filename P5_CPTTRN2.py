#http://www.spoj.com/problems/CPTTRN2/
from __future__ import print_function
def printingFunction(l,c):
	for i in range(0,l):
		for j in range(0,c):
			if(i==0 or j==0 or i==l-1 or j==c-1):
				print("*",sep='',end='')
			else:
				print('.',sep='',end='')
		print('\n')
t=input()
for i in range(0,t):
	l,c = map(int, raw_input().split())
	if l<=2:
		for j in range(0,l):
			for k in range(0,c):
				print('*', end='')
			print('\n')
	else:
		printingFunction(l,c)
print('\n')
