import sys

n_clients, n_data = tuple(int(x) for x in sys.stdin.readline().split())
s_cost, l_cost = tuple(int(x) for x in sys.stdin.readline().split())
client_costs = []
    
for i in range(n_clients):
    n_small, n_large = tuple(int(x) for x in sys.stdin.readline().split())
    ind_val = (i+1, n_small * s_cost+ l_cost * n_large)
    client_costs.append(ind_val)

client_costs.sort(key=lambda x:x[1])
solution, cur_index = [], 0

for (client_num, cost) in client_costs:
    if n_data - cost >= 0:
        n_data -= cost
        solution.append(client_num)
    else:
        break

print(len(solution))
for num in solution:
    print(num)
