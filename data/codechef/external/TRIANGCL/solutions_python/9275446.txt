import math 
id = input()
t = input()

def equals(a,b):
	if (abs(a-b) < 0.000001):
		return True ; 
	return False ; 

def dist(x1,y1,x2,y2): 
	return math.sqrt((x1-x2)**2+(y1-y2)**2) ; 

while (t!=0) : 
	s = raw_input()
	s1 = s.split(" ") 
	x1 = int(s1[0]) 
	y1 = int(s1[1])
	x2 = int(s1[2]) 
	y2 = int(s1[3])
	x3 = int(s1[4]) 
	y3 = int(s1[5])

	l = []
	l.append(dist(x1,y1,x2,y2))
	l.append(dist(x2,y2,x3,y3))
	l.append(dist(x3,y3,x1,y1))
	l.sort()
	a = l[0]
	b = l[1]
	c = l[2]

	if (id == 1):
		if (equals(a,b) | equals(b,c) | equals(c,a)):
			print "Isosceles triangle" 
		else : 
			print "Scalene triangle"
	if (id == 2):
		if (equals(a,b) | equals(b,c) | equals(c,a)):
			print "Isosceles",
			if (equals(a**2+b**2,c**2)):
				print "right triangle"
			elif (a**2+b**2 > c**2):
				print "acute triangle"
			else :
				print "obtuse triangle"
		else : 
			print "Scalene",
			if (equals(a**2+b**2,c**2)):
				print "right triangle"
			elif (a**2+b**2 > c**2):
				print "acute triangle"
			else :
				print "obtuse triangle"
	t-= 1