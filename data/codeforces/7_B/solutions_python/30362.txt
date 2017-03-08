from sys import stdin

def ints(s):
    return [int(x) for x in s.split()]

t, m = ints(stdin.readline())

mem = [0 for i in range(m+2)]

next_id = 1

def alloc(size):
    global mem
    global next_id
    i = 1
    while (i <= m):
        if mem[i] == 0:
            j = i + 1
            while (j < i + size and j <= m and mem[j] == 0):
                j += 1
            if j - i == size:
                for k in range(i, j):
                    mem[k] = next_id
                print(next_id)
                next_id += 1
                return
            i = j + 1
        else:
            i += 1
    print("NULL")

def erase(x):
    global mem
    mem[m+1] = x
    i = mem.index(x)
    mem[m+1] = 0
    if i == m+1 or x == 0:
        print("ILLEGAL_ERASE_ARGUMENT")
        return
    while i <= m and mem[i] == x:
        mem[i] = 0
        i += 1

def defragment():
    global mem
    mem = [0] + [x for x in mem if x != 0]
    k = m + 2 - len(mem)
    mem = mem + [0 for x in range(k)]
    assert(len(mem) == m+2)

for i in range(t):
    xs = stdin.readline().split()
    if xs[0] == "alloc":
        alloc(int(xs[1]))
    elif xs[0] == "erase":
        erase(int(xs[1]))
    elif xs[0] == "defragment":
        defragment()
    else:
        while (True): pass