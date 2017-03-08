n, k = map(int, raw_input().split())
x = map(int, raw_input().split())
sum = [0]
for i in range(1, n + 1):
    sum.append(sum[i - 1] + x[i - 1])
ksum = [0]
for i in range(1, n - k + 2): 
    ksum.append(sum[i + k - 1] - sum[i - 1])
right = [0 for i in ksum]
pos = [0 for i in ksum]
right[len(ksum) - 1] = ksum[len(ksum) - 1]
pos[len(ksum) - 1] = len(ksum) - 1
for i in range(len(ksum) - 2, 0, -1):
    if ksum[i] >= right[i + 1]:
        right[i] = ksum[i]
        pos[i] = i
    else:
        right[i] = right[i + 1]
        pos[i] = pos[i + 1]
ans = -1
a = -1
for i in range(1, len(ksum) - k):
    if (ksum[i] + right[i + k] > ans):
        ans = ksum[i] + right[i + k]
        a = i
b = pos[a + k]
print(str(a) + " " + str(b))
