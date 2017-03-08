T = int(raw_input())

for i in range(T):
    N = int(raw_input())
    x = map(int, raw_input().split())
    
    # Because we can always find the minimum of all numbers and then
    # group it left or right to eliminate the other elements
    # and cost would always equal that minimum number
    # Total number of operations to reduce from N to 1 is N-1
    # Therefore total cost = minimum * (N-1)
    
    minimum = min(x)
    cost = minimum * (N-1)
    
    print cost
