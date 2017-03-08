n = int(input())
start = 0
finish = 10**8
while start < finish:
    middle = (start + finish) // 2 + 1
    cnt = middle * (middle + 1) / 2
    if cnt < n:
        start = middle
    else:
        finish = middle - 1
answer = n - start * (start + 1) // 2
print(answer)
