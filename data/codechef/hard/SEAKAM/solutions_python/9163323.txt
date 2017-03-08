import itertools
MODULO=1000000007
visited = [0] * 100001
count_connected_components = 0
#functions
def depth_first_traversal(graph, node, visited):
	stack = []
	visited[node] = 1
	stack.extend(graph[node])
	while len(stack) != 0:
		seed = stack.pop()
		if not visited[seed]:
			visited[seed] = 1
			stack.extend(graph[seed])
	
def connected_components(graph):
	global count_connected_components, visited
	count_connected_components = 0
	count_indegree_1 = 0
	bInvalid = False
	for node in graph:
		if not visited[node]:
			count_connected_components += 1
			depth_first_traversal(graph, node, visited)
	for node in graph:
		if len(graph[node]) > 2:
			bInvalid = True
		elif len(graph[node]) == 1:
			count_indegree_1 += 1
		visited[node] = 0
	if bInvalid or (count_indegree_1 != 2 * count_connected_components):
		return -1
	return count_connected_components

def find_count(edges, N):
	#prepare the adjacency graph
	global count_connected_components
	graph = {}
	for e in edges:
		if e[0] in graph:
			graph[e[0]].append(e[1])
		else:
			graph[e[0]] = [e[1]]
		if e[1] in graph:
			graph[e[1]].append(e[0])
		else:
			graph[e[1]] = [e[0]]
	count_connected_components = connected_components(graph)
	if count_connected_components == -1:
		return 0
	connected_components_including_solo_vertices = N - len(graph) + count_connected_components
	#calculate connected_components_including_solo_vertices!
	fact_connected_components_including_solo_vertices = fact_n[connected_components_including_solo_vertices]
	answer = fact_connected_components_including_solo_vertices
	answer *= (1 << count_connected_components)
	answer %= MODULO
	return answer

def process_case(N, M):
	sign = 1
	global fact_n
	#read list of edges, call it gaps
	#print fact_n
	gaps = []
	for i in range(M):
		e1, e2 = raw_input().split()
		e1, e2 = int(e1), int(e2)
		if e1 != e2:
			gaps.append([e1, e2])
	
	removed_edges = 0
	for n_m in range(1, M+1):
		combination_of__n_m = list(itertools.combinations(gaps, n_m))
		for combination in combination_of__n_m:
			count = find_count(combination, N)
			#print count, combination, sign
			removed_edges = (removed_edges + sign * count) #% MODULO
		#toggle the sign after value of n_m increases
		sign *= -1

	#to avoid negative answer
	answer = fact_n[N]
	answer += MODULO
	#if removed_edges < 0:
	#	removed_edges += MODULO
	#print "removed edges:" + str(removed_edges)
	fact = answer - removed_edges + MODULO
	fact = fact % MODULO
	return fact
			
#main program
#calculate n! modulo MODULO
fact_n = [0] * 100001
fact_n[1] = 1
for i in range(2, 100001):
	fact_n[i] = (i * fact_n[i-1]) % MODULO

T = int(raw_input())

for test_case in range(T):
	N, M = raw_input().split()
	N, M = int(N), int(M)

	print process_case(N, M)