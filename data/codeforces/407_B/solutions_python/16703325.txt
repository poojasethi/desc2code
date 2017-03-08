
# coding: utf-8

# # B. Long Path
# 
# - time limit per test: 1 second
# - memory limit per test: 256 megabytes
# - input: standard input
# - output: standard output
# 
# One day, little Vasya found himself in a maze consisting of (n + 1) rooms, numbered from 1 to (n + 1). Initially, Vasya is at the first room and to get out of the maze, he needs to get to the (n + 1)-th one.
# 
# The maze is organized as follows. Each room of the maze has two one-way portals. Let's consider room number i (1 ≤ i ≤ n), someone can use the first portal to move from it to room number (i + 1), also someone can use the second portal to move from it to room number pi, where 1 ≤ pi ≤ i.
# 
# In order not to get lost, Vasya decided to act as follows.
# 
# - Each time Vasya enters some room, he paints a cross on its ceiling. Initially, Vasya paints a cross at the ceiling of room 1.
# 
# - Let's assume that Vasya is in room i and has already painted a cross on its ceiling. Then, if the ceiling now contains an odd number of crosses, Vasya uses the second portal (it leads to room pi), otherwise Vasya uses the first portal. 
# 
# Help Vasya determine the number of times he needs to use portals to get to room (n + 1) in the end.
# 
# #### Input
# 
# The first line contains integer n (1 ≤ n ≤ 103) — the number of rooms. The second line contains n integers pi (1 ≤ pi ≤ i). Each pi denotes the number of the room, that someone can reach, if he will use the second portal in the i-th room.
# 
# #### Output
# 
# Print a single number — the number of portal moves the boy needs to go out of the maze. As the number can be rather large, print it modulo 1000000007 (109 + 7).
# 
# #### Examples
# 
# Input
# ```
# 2
# 1 2
# ```
# 
# Output
# ```
# 4
# ```
# 
# Input
# ```
# 4
# 1 1 2 3
# ```
# 
# Output
# ```
# 20
# ```
# 
# Input
# ```
# 5
# 1 1 1 1 1
# ```
# 
# Output
# ```
# 62
# ```

# ### Standard Input Generator

# In[66]:

import sys


def example_generator(line):
    """Read example from stdin and parse it into the appropriate data structure
    
    Use in the following way:
    
    example = example_generator(stdin_generator)
    while True:
        numbers, target = next(example)
        .
        .
        .
    
    """
    while True:
        n = int(next(line).strip())
        P = [int(p_i)-1 for p_i in next(line).split()] # convert to zero-indexing
        
        yield n, P


# ### Workhorse Functions

# In[68]:

def do_maze(n, p):
    """Print out the number of times Vasya needs to use portals to get to room n+1
    
    dp[i] is the number of portal jumps required to start off at room i with an odd
    number of crosses and get back to room i with an even number of crosses.
    
    Hence the recurrence relation is as follows:
    
    dp[i] = 1 + [Sum_{j = p(i)}^{i-1} dp[j] + 1]
    
    This can be read as "the number of portal jumps to get from room i with an odd
    number of crosses to an even number of crosses is equivalent to taking a portal
    jump to room p(i) into an odd number of crosees (+1), getting back into that
    state with an even number of crosses (Sum part).
    
    """
    dp = [0]*n
    
    for i in range(n):
        
        portal_jumps = 1 # initial jump from from i to p[i]
        
        # This block would read cleaner if it was just a for loop!
        for j in range(p[i], i):
            portal_jumps += (dp[j] % (1e9+7)) # jumps to get you from room j with odd to room j with even
            portal_jumps += (1 % (1e9+7)) # extra jump to get you from j to j+1
            
        dp[i] = int(portal_jumps % (1e9+7))
        
    total_pjumps = 0    
    for i in range(n):
        total_pjumps += (dp[i] % (1e9+7))
        total_pjumps += (1 % (1e9+7))
        
    print(int(total_pjumps % (1e9+7)))


example = example_generator(sys.stdin)

if __name__ == '__main__':
    n, P = next(example)

    do_maze(n, P)
