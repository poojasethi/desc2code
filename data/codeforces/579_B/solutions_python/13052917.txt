n = int(raw_input())
teams = []

for a in xrange(1, 2*n):
    scores = map(int, raw_input().split())
    for b in xrange(0, a):
        teams.append((scores[b], a, b))

pair = [-1]*(2*n)
teams.sort(key = lambda x: - x[0])
for team in teams:
    if pair[team[1]] == -1 and pair[team[2]] == -1:
        pair[team[1]] = team[2]
        pair[team[2]] = team[1]

print ' '.join(map(lambda x: str(x + 1), pair))
