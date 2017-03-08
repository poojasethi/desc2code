__author__ = 'trunghieu11'


def solve(n, vertex):
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += abs(vertex[i][0] - vertex[j][0]) * abs(vertex[i][1] - vertex[j][1])
    return -1 if answer == 0 else answer / (2 * (max(1, n - 2)));



if __name__ == '__main__':
    n = int(raw_input())
    vertex = []
    for i in range(n):
        vertex.append(map(int, raw_input().split(" ")))
    print solve(n, vertex)