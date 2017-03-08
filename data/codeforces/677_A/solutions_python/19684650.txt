n,h=map(int,raw_input().split())
integers=map(int,raw_input().split())

def high(x):
	return x>h

integer=filter(high,integers)
print len(integer)+n