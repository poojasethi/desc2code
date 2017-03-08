import re

inp = raw_input()

X = inp.replace(',', ';')

x = X.split(';')

a = ""
b = ""
A = []
B = []

for i in x:
	if(i.isdigit() == True):
		if( i == str(int(i))):
			a += i
			A += i
			a += ','
		else:
			b += i
			B += i
			b += ','
	else:
		b += i
		b += ','
		B += i
		if i == '':
			B += ' '

a = a[:-1]
b = b[:-1]

if(len(A) == 0): 
	a = '-'
else:
	a = '"' + a + '"'	
if(len(B) == 0): 
	b = '-'
else:
	b = '"' + b + '"'
#print x
print a#, A
print b#, B