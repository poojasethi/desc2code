one_hole = ['A', 'D', 'O', 'P', 'Q', 'R']
two_holes = ['B']

t = int(raw_input())
for x in range(t):
    s = list(raw_input())
    count = 0
    for i in s:
        if i in one_hole:
            count += 1
        elif i in two_holes:
            count += 2
    print count
