from collections import deque

def main():
	n = input()
	Q = deque()
	for x in xrange(n):
		Q.appendleft(raw_input())
	S = set()
	for s in Q:
		if s not in S:
			S.add(s)
			print s

if __name__ == '__main__':
	main()
