#http://codeforces.com/problemset/problem/555/A
n, k = map(int, raw_input().split())

result = 0
distinct = []
 
#tirando elementos
for i in range(k):
	chain = map(int, raw_input().partition(" ")[2].split())
	continuos = [1]
	for j in range(1, len(chain)):
		if(chain[j]-1 == continuos[-1]):
			continuos.append(chain[j])
		else:
			result += 1
			distinct.append(chain[j])

result += k -1
result += len(distinct)
print result
