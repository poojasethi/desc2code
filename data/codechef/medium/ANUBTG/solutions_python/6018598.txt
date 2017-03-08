#!/usr/bin/python
import math

def pay_per_bill(array):
	"This gives sum of first two elements of the array"
	array_size = len(array)
	if array_size>=2:
		return array[0]+array[1]
	elif array_size==1:
		return array[0]
	else:
		return 0

T = int(raw_input())
ans_array = []
max_count = 0

case=0
while (case<T):
	eq_no = 'NO EQUILIBRIUM'
	n=int(raw_input())
	cost_array = sorted(map(int,raw_input().split()),reverse=True)
	bills = int(math.ceil(len(cost_array)/4.0))
	i=0
	final = 0
	while i<bills:
		ith_bill = cost_array[4*i:4*(i+1)]
		final += pay_per_bill(ith_bill)
		i+=1
	print final
	case = case+1