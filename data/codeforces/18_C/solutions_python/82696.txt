n = int(raw_input())
numbers = map(int, raw_input().strip().split())
sum = sum(numbers)
count = 0
tot = 0.0
for i in xrange(len(numbers) - 1):
    tot += numbers[i]
    if (tot == float(sum)/2.0):
        count += 1

print count
            
