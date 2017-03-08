#! /usr/bin/python
foo = sorted(map(int, raw_input().split()))
bar="IMPOSSIBLE"
if foo[2] <= foo[0] + foo[1] or foo[3] <= foo[1] + foo[2]:
	bar="SEGMENT"
if foo[0] + foo[1] > foo[2] or foo[1] + foo[2] > foo[3]:
	bar="TRIANGLE"
print bar
