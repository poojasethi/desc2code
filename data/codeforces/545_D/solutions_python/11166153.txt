n = int(raw_input())
arr = [int(x) for x in raw_input().split()]

ctr = 0
arr.sort()
wait = 0
for i in range(len(arr)):
	if wait <= arr[i]:
		ctr += 1
		wait += arr[i]

print min(ctr, len(arr))
