n, A = map(int, raw_input().split())
D = map(int, raw_input().split())

s = sum(D)
B = map(lambda x: x-(min(x, A-(n-1))-max(1, A-(s-x))+1), D)
print ' '.join(map(str, B))
