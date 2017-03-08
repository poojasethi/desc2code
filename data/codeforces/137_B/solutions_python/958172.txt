n = input()
nums = [int(x) for x in raw_input().split()]

count = 0
for i in xrange(1, n+1):
    if i not in nums:
        count += 1

print count
