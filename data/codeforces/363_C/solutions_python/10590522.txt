#!/usr/bin/env python

import sys

def solve(line):
	result = []
	i = 0

	previous_cnt = 0
	while i < len(line):
		character = line[i]

		cnt = 0
		while i < len(line) and character == line[i]:
			cnt += 1
			i += 1

		if cnt < 2:
			result.append(character)
			previous_cnt = 1
		else:
			if previous_cnt < 2:
				result += [character] * 2
				previous_cnt = 2
			else:
				result.append(character)
				previous_cnt = 1
		
	return ''.join(result)

def test():
	print solve("helloo")
	print solve("woooooow")
	print solve("aaabb")
	print solve("aabbccdd")
	quit()

if __name__ == "__main__":
	line = sys.stdin.readline()

	print solve(line)
