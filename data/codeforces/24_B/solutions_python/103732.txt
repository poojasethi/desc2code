#!/usr/bin/env python

t = int(raw_input())
scores = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1] + 50*[0]
racers = {}
class racer:
    def __init__(self, name):
        self.score = 0
        self.places = 50*[0]
        self.name = name

for k in range(t):
    n = int(raw_input())
    for i in range(n):
        name = raw_input()
        racers[name] = racers.get(name, racer(name))
        racers[name].score += scores[i]
        racers[name].places[i] += 1

def msc(l):
    res = 0;
    for r in l:
        res = max(res, r.score)
    return res

def mpl(l, i):
    res = 0
    for r in l:
        res = max(res, r.places[i])
    return res

first = racers.values()
first_tmp = []
max_sc = msc(first)
for r in first:
    if r.score == max_sc:
        first_tmp.append(r)
first, first_tmp = first_tmp, []
for i in range(50):
    max_pl = mpl(first, i)
    for r in first:
        if r.places[i] == max_pl:
            first_tmp.append(r)
    first, first_tmp = first_tmp, []
print first[0].name

second = racers.values()
second_tmp = []
max_pl = mpl(second, 0)
for r in second:
    if r.places[0] == max_pl:
        second_tmp.append(r)
second, second_tmp = second_tmp, []
max_sc = msc(second)
for r in second:
    if r.score == max_sc:
        second_tmp.append(r)
second, second_tmp = second_tmp, []
for i in range(1, 50):
    max_pl = mpl(second, i)
    for r in second:
        if r.places[i] == max_pl:
            second_tmp.append(r)
    second, second_tmp = second_tmp, []
print second[0].name
