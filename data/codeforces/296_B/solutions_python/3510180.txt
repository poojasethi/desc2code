n = raw_input()
n = int(n)
A = raw_input()
B = raw_input()

flag_1 = 0
flag_2 = 0
cnt = 0
for i in xrange(n):
    if A[i] == '?':
        cnt += 1
    if B[i] == '?':
        cnt += 1

    if A[i] == '?' or B[i] == '?':
        pass
    elif ord(A[i]) < ord(B[i]):
        flag_1 = 1
    elif ord(A[i]) > ord(B[i]):
        flag_2 = 1


if flag_1 and not flag_2:
    s = 1
    for i in xrange(n):
        if A[i] == '?' and B[i] == '?':
            s *= 55
        elif A[i] == '?':
            s *= ord(B[i]) - ord('0') + 1
        elif B[i] == '?':
            s *= ord('9') - ord(A[i]) + 1

    s = 10 ** cnt - s

elif flag_2 and not flag_1:
    s = 1
    for i in xrange(n):
        if A[i] == '?' and B[i] == '?':
            s *= 55
        elif A[i] == '?':
            s *= ord('9') - ord(B[i]) + 1
        elif B[i] == '?':
            s *= ord(A[i]) - ord('0') + 1
    s = 10 ** cnt - s

elif flag_2 + flag_1 == 0:
    s = 1
    for i in xrange(n):
        if A[i] == '?' and B[i] == '?':
            s *= 55
        elif A[i] == '?':
            s *= ord(B[i]) - ord('0') + 1
        elif B[i] == '?':
            s *= ord('9') - ord(A[i]) + 1

    t = s
    s = 1

    for i in xrange(n):
        if A[i] == '?' and B[i] == '?':
            s *= 55
        elif A[i] == '?':
            s *= ord('9') - ord(B[i]) + 1
        elif B[i] == '?':
            s *= ord(A[i]) - ord('0') + 1

    a = 1
    for i in xrange(n):
        if A[i] == '?' and B[i] == '?':
            a *= 10

    s = 10 ** cnt - s - t + a

elif flag_1 + flag_2 == 2:
    s = 10 ** cnt

print s % 1000000007

