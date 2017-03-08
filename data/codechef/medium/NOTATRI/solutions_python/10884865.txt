def sum_pair_less_than(v, S):
	i,j,pair_count = 0,len(v)-1,0
	while i < j:
		if v[i]+v[j] < S :
			pair_count += j-i
			i+=1
		else:
			j-=1
	return pair_count

def not_a_triangle_count(v):
	non_tri_count = 0
	v.sort()
	i=len(v)-1
	while i >= 2 :
		non_tri_count += sum_pair_less_than(v[0:i],v[i])
		i-=1
	return non_tri_count

while True:
	n = input()
	if n==0 :
		exit()
	v = [int(x) for x in raw_input().split(' ')]
	print not_a_triangle_count(v)