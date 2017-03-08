n = int(raw_input())

h = [int(x) for x in raw_input().split()]

maxr = [0] * n
add = [0] * n

i = n-2
while i >= 0:
    maxr[i] = max(maxr[i+1], h[i+1])
    add[i] = max(0, maxr[i] - h[i] + 1)
    i -= 1

result = ' '.join([str(item) for item in add])
result = result.strip()
print result
