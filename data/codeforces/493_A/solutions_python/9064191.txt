hm = raw_input()
aw = raw_input()
n = int(raw_input())

yellows = []
seenreds = []
reds = []

for x in range(n):
    m, t, p, c = raw_input().split(" ")
    if (c == "r" or ((t+p) in yellows)) and (not (t+p) in seenreds):
        seenreds = seenreds + [t+p]
        reds = reds + [(hm if t == "h" else aw) + " " + p + " " + m]
    else:
        yellows = yellows + [t+p]

for x in reds:
    print x

