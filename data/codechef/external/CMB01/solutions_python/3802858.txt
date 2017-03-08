#!/usr/bin/env python

import math

def addrev(num):
	c = 0
	while num > 0:
		c = c * 10 + int(num) % 10
		num =  int(num) / 10
	return c
	
if __name__ == '__main__':
	testcase = int(raw_input())
	while testcase > 0:
		num1, num2 = raw_input().split()
		sum = addrev(num1) + addrev(num2)
		sum = addrev(sum)
		print sum
		testcase = testcase - 1
	
