'''
Created on 2/05/2014

@author: milderhc
'''
import sys

def add(G, a, b):
    for c, d in G:
        if (c < a and a < d) or (c < b and b < d):
            make_link(G, a, b, c, d)
        if (a < c and c < b) or (a < d and d < b):
            make_link(G, c, d, a, b) 

def make_link(G, a, b, c, d):
    G[(a, b)][(c, d)] = 1
    
def answer(G, list, a, b):
    start = list[a-1]
    end = list[b-1]
    marked = {}
    marked[start] = 1
    queue = [start]
    while queue <> []:
        current = queue.pop(0)
        for nb_a, nb_b in G[current]:
            if (nb_a, nb_b) == end:
                return 'YES'
            if (nb_a, nb_b) not in marked:
                marked[(nb_a, nb_b)] = 1
                queue.append( (nb_a, nb_b) )
    
    return 'NO'

G = {}
list = []
n = int( sys.stdin.readline().strip() )
while n > 0:
    input = sys.stdin.readline().strip().split()
    c = int( input[0] )
    x = int( input[1] )
    y = int( input[2] )
    
    if c == 1:
        G[(x,y)] = {}
        add(G, x, y)
        list.append( (x, y) )
    else:
        print answer(G, list, x, y)
    n -= 1
    
