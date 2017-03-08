n, last = int(raw_input()), 0
exams = sorted([map(int, raw_input().split()) for _ in xrange(0, n)])
for exam in exams:
    if exam[1] >= last:
        last = exam[1]
    else:
        last = exam[0]
print last
