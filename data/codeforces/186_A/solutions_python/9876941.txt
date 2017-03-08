#!/usr/bin/python

def main():
	difference=0
	first=raw_input()
	second=raw_input()

	for i in range(0, min(len(first), len(second))):
		if first[i]!=second[i]:
			difference+=1

	if ''.join(sorted(first))==''.join(sorted(second)) and difference==2:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()