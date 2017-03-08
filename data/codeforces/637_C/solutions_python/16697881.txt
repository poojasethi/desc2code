n = int(raw_input())

promos = []
for i in range(n):
	promos.append(raw_input())

pairs = [(i,j) for i in range(0,6) for j in range(i+1, 6)]

def promo_without(promo,i,j):
	pw = list(promo)
	del(pw[j], pw[i])
	return tuple(pw)

if n == 1:
	print 6
	exit()

for i,j in pairs:
	comp = lambda x : promo_without(x,i,j)
	promos.sort(key = comp)
	
	for k in range(1,n):
		if comp(promos[k]) == comp(promos[k-1]):
			print 0
			exit()

for i,j in pairs:
	comp = lambda x : (x[i], x[j])
	promos.sort(key = comp)
	
	for k in range(1,n):
		if comp(promos[k]) == comp(promos[k-1]):
			print 1
			exit()

print 2
