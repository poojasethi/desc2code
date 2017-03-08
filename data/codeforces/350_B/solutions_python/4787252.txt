#! /usr/bin/python

import sys

MTN, HOTEL = 0, 1

def dfs(hotel_idx, types, paths, out_degree_map):
    best_path = [hotel_idx]
    parent = paths[hotel_idx - 1]
    while parent != 0 and out_degree_map.get(parent, 0) == 1:
        best_path.append(parent)
        parent = paths[parent - 1]
    best_path.reverse()
    return {'length': len(best_path), 'paths': best_path}

if __name__ == '__main__':
    sys.stdin.readline()
    types = map(int, sys.stdin.readline().split())
    paths = map(int, sys.stdin.readline().split())
    out_degree_map = {}
    for i in range(len(paths)):
        parent = paths[i]
        if parent != 0:
            out_degree_map[parent] = out_degree_map.get(parent, 0) + 1

    result = [dfs(i + 1, types, paths, out_degree_map) for i in range(len(types)) if types[i] == HOTEL]
    result.sort(lambda a, b: a['length'] - b['length'])
    best = result[-1]
    print best['length']
    print ' '.join([str(i) for i in best['paths']])
