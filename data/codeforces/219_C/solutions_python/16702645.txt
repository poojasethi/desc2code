# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:06:09 2016

@author: Mary
"""

import string


def repaint_groups3same(s):

    num_repaints = 0

    for i in range(1, len(s)-1):
        if s[i-1] == s[i] == s[i+1]:
            s[i] = int(s[i] == 0)
            num_repaints += 1

    return num_repaints


def repaint_groups3diff(s):

    num_repaints = 0

    for i in range(1, len(s)-1):
        if s[i-1] == s[i] or s[i] == s[i+1]:
            for letter in range(3):
                if s[i-1] != letter and s[i+1] != letter:
                    break
            s[i] = letter
            num_repaints += 1

    return num_repaints


def repaint_dp(s):

    # Find minimum number of repaints for each letter in s
    # minnr[i][0] -- num min repaints to make current letter to be A
    # minnr[i][1] -- num min repaints to make current letter to be B
    minnr = [[0, 0] for i in range(len(s))]

    idx2change = int(s[0] == 0)
    minnr[0][idx2change] = 1

    for i in range(1, len(s)):

        minnr[i][0] = minnr[i-1][1]
        minnr[i][1] = minnr[i-1][0]

        minnr[i][not s[i]] += 1

    # Find min number of repaints for all s
    num_repaints = min(minnr[-1])

    # Repaint s
    cur_l = num_repaints != minnr[-1][0]

    for i in range(len(s)-1, -1, -1):
        s[i] = cur_l
        cur_l = not cur_l

    return num_repaints


#input_file = 'C:\Users\Mary\Documents\input.txt'
input_file = ''

if input_file:
    f = open(input_file, 'r')
    n, k = map(int, f.readline().strip().split())
    input_s = f.readline().strip()
else:
    n, k = map(int, raw_input().strip().split())
    input_s = raw_input().strip()

s = [ord(c) - ord('A') for c in input_s]

num_repaints = 0

if len(s) == 2:
    if s[0] == s[1]:
        num_repaints = 1
        s[0] = not s[0]
elif len(s) > 2:
    if k == 2:
        num_repaints = repaint_dp(s)
    else:
        num_repaints = repaint_groups3same(s)
        num_repaints += repaint_groups3diff(s)

out_s = [chr(i + ord('A')) for i in s]

print(num_repaints)
print(string.join(out_s, ''))
