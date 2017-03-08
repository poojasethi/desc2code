# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 574B - B. Bear and Three Musketeers
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# number of warriors and number of pairs of warriors knowing each other
n, m = map(int, raw_input().split())

# auxiliary list to the count of warriors' adjacency
graph = [set() for vertex in xrange(n)]

# list of possibles choices of the three musketeers
choices = []

for i in xrange(m):
    a, b = map(int, raw_input().split())
    graph[a-1].add(b - 1)
    graph[b-1].add(a - 1)

    intersection = graph[a-1].intersection(graph[b-1])
    if intersection:
        for j in intersection:
            choice = set([a-1, j, b-1])
            choices.append(choice)

if not choices:
    print -1
else:
    lower_cardinality = float('inf')
    # cardinality default of one member to the three musketeers
    default_cardinality = -2
    for choice in choices:
        minimum = 0
        while choice:
            vertex = choice.pop()
            minimum += len(graph[vertex]) + default_cardinality

        if minimum < lower_cardinality:
            lower_cardinality = minimum

    print lower_cardinality
