# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 553A - A. Kyoya and Colored Balls
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

MOD = 1000000007

def get_colors_comb(n=2000):
    c = [[0] * n for l in xrange(n)]
    for i in xrange(n):
        c[i][0] = c[i][i] = 1
        for j in xrange(i):
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

    return c

k = int(raw_input())
colors = get_colors_comb()

temp = 0
answer = 1
for i in xrange(1, k + 1):
    ball = int(raw_input())
    a = temp + 1
    b = ball - 1

    temp += ball
    answer = answer * colors[a + b - 1][a - 1] % MOD

print answer