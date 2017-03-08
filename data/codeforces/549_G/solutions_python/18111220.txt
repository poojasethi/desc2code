#http://codeforces.com/problemset/problem/549/G
n = int(raw_input())
flag = False
nums = map(int, raw_input().split())
for i in range(n):
	nums[i] += i;
nums.sort()
for i in range(n-1):
	if(nums[i]-i > nums[i+1]-i-1):
		print ":("
		flag = True
		break

answer = ""
if(not flag):
	for i in range(n):
		answer += str(nums[i]-i)
		if(i != n-1):
			answer += " "

	print answer