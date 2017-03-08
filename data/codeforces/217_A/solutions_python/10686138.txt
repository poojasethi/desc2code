n = int(raw_input())

pos = [0]*105

graph = {}

def get_input():
	node_number = 1
	
	for node in range(n):
		x,y = map(int,raw_input().split())
		
		pos[node_number] = ((x,y))
		
		node_number += 1

def make_graph():
	for node in range(1, n+1):
		graph_node = pos[node]
		
		if node not in graph.keys():
			graph[node] = []
		
		for j in range(node+1, n+1):
			second_graph_node = pos[j]
			if graph_node[0] == second_graph_node[0] or graph_node[1] == second_graph_node[1]:
				graph[node].append(j)
				if j not in graph.keys():
					graph[j] = [node]
				else:
					graph[j].append(node)

def dfs(node, color, node_colors):
    node_colors[node] = color
    for child in graph[node]:
        if node_colors[child] != color:
            dfs(child, color, node_colors)

def components_number():
    node_colors = [-1] * (n+1)

    color = 0
    for node in range(1, n+1):
        if node_colors[node] == -1:
            dfs(node, color, node_colors)

            color += 1
    
    return color-1

def main():
	get_input()
	make_graph()
	print components_number()

main()
