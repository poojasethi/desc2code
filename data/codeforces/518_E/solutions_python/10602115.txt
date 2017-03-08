#!/usr/bin/env python

import sys

MAX = 1E10
MIN = -1E10

class Value():
    def __init__(self, v):
        if v != '?':
            self.set_value(int(v))
        else:
            self.value = None
            self.min_bound = MIN
            self.max_bound = MAX

    def set_value(self, v):
        self.value = v
        self.min_bound = v
        self.max_bound = v

    def is_fixed(self):
        return self.value is not None

    def to_string(self):
        return str(self.value)

    def detail(self):
        return "value: %s, min: %s, max: %s" % (self.value, self.min_bound, self.max_bound)

    def update_with_left(self, left):
        if left.is_fixed():
            if left.value >= 0:
                self.set_value(left.value + 1)
            else:
                self.min_bound = left.value + 1
        else:
            self.min_bound = left.min_bound + 1

    def update_with_right(self, right):
        if right.is_fixed():
            if right.value <= 0:
                self.set_value(right.value - 1)
            else:
                self.max_bound = right.value - 1
        else:
            self.max_bound = right.max_bound - 1


def is_meet_property(seq, n, k):
    # Ai < Ai+k < Ai+2k < ...
    for i in range(k):
        for j in range(i, n - k, k):
            left = seq[j]
            right = seq[j + k]
            if not left.is_fixed() or not right.is_fixed():
                return False
            if left.value >= right.value:
                return False
    return True


def update_value(seq, index, n, k):
    middle = seq[index]
    left_index, right_index = index - k, index + k
    left = seq[left_index] if left_index > -1 else None
    right = seq[right_index] if right_index < n else None
    if left is not None:
        middle.update_with_left(left)
    if right is not None:
        middle.update_with_right(right)


def update_right_direction(seq, n, k):
    for i in range(n):
        value = seq[i]
        if value.is_fixed():
            continue
        update_value(seq, i, n, k)


def update_left_direction(seq, n, k):
    for i in range(n - 1, -1, -1):
        value = seq[i]
        if value.is_fixed():
            continue
        update_value(seq, i, n, k)


def restore_constraint_without_fixed(seq, n, k):
    for i in range(k):
        constraint = [ seq[j] for j in range(i, n, k) ]
        if reduce( lambda x,y: x and y, map(lambda x: not x.is_fixed(), constraint)):
             offset = len(constraint) / 2
             for i, v in enumerate(constraint):
                v.set_value(i - offset)


def determine_pending_value(seq, n, k):
    for i in range(k):
        pendings = [ seq[j] for j in range(i, n, k) if not seq[j].is_fixed() ]
        pending_first = None
        for i, v in enumerate(pendings):
            if pending_first is None:
                pending_first = v
                offset = - (len(pendings) / 2)
                #if v.min_bound > v.max_bound:
                    #print 'Error!'
                if 0 <= v.min_bound :
                    v.set_value(v.min_bound)
                elif v.max_bound <= 0:
                    v.set_value(v.max_bound)
                else:
                    v.set_value(offset if v.min_bound <= offset else v.min_bound)
            else:
                v.set_value(pending_first.value + i)


def restore(seq, n, k):

    restore_constraint_without_fixed(seq, n, k)

    update_right_direction(seq, n, k)
    update_left_direction(seq, n, k)

    determine_pending_value(seq, n, k)
    #print '\n'.join(map(Value.detail, seq))


def solve():
    n, k = map(int, sys.stdin.readline().rstrip().split(' '))
    sequence = map(Value, sys.stdin.readline().rstrip().split(' '))

    restore(sequence, n, k)
    if is_meet_property(sequence, n, k):
        print ' '.join(map(Value.to_string, sequence))
    else:
        print 'Incorrect sequence'


if __name__ == '__main__':
    solve()

