import fileinput
import itertools
import sys
import random

''' http://www.codechef.com/problems/DIVSUBS '''

def single_test_dumb(nums):
	nums = [(index, int(x)) for index,x in enumerate(fi.readline().strip().split(" "))]

	for i in range(1, len(nums)+1):
		for pairs in itertools.combinations(nums, i):
			if sum(x[1] for x in pairs) % n == 0:
				print len(pairs)
				print ' '.join(str(x[0]+1) for x in pairs)
				return

def single_test_smart(nums):
	n = len(nums)

	sums = [nums[0][1]]
	for idx in range(1, n):
		sums.append((sums[idx-1] + nums[idx][1]))

	sums = [x % n for x in sums]

	rems = {}
	for index, x in enumerate(sums):
		if x == 0:
			print index+1
			print ' '.join(str(x+1) for x in range(index+1))
			return

		if x in rems:
			#assert((sum(x[1] for x in nums[rems[x]+1:index+1]) % n) == 0)
			#print sum(x[1] for x in nums[rems[x]+1:index+1]) % n, sum(x[1] for x in nums[rems[x]+1:index+1])
			#print nums[rems[x]+1:index+1]
			print index - rems[x]
			print ' '.join(str(x+1) for x in range(rems[x]+1, index+1))
			return
		rems[x] = index
	print -1

def main():
	if len(sys.argv) > 1:
		togen = int(sys.argv[1])
		print 1
		print togen
		print ' '.join(str(random.randint(1, 10**9)) for x in range(togen))
		return

	fi = fileinput.input()
	numtests = int(fi.readline())

	for i in range(numtests):
		n = int(fi.readline())
		nums = [(index, int(x)) for index,x in enumerate(fi.readline().strip().split(" "))]
		single_test_smart(nums)


if __name__ == '__main__':
	main()