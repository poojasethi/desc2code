from collections import deque

n = input()
t = map(int, raw_input().split())
dq = deque(t)
cntA = cntB = 0
sumA = sumB = 0

while True:
    if len(dq) == 0:
        break
    else:
        if sumA > sumB:
            sumB += dq.pop()
            cntB += 1
        elif sumA < sumB:
            sumA += dq.popleft()
            cntA += 1
        else:
            if len(dq) == 1:
                cntA += 1
                break
            else:
                sumA += dq.popleft()
                cntA += 1
                sumB += dq.pop()
                cntB += 1

print cntA, cntB
