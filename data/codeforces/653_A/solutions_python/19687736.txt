from itertools import groupby
from operator import itemgetter

n=int(raw_input())
integers=map(int,raw_input().split())
integers=sorted(list(set(integers)))

def func():
	for k,g in groupby(enumerate(integers),lambda (i,x):i-x):
		if len(map(itemgetter(1),g))>2:
			print "YES"
			return 0
	print "NO"

func()