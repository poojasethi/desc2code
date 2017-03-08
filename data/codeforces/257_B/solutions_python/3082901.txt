from sys import stdin

v = [int(x) for x in stdin.readline().strip().split()]

# v[0] is the count of the less, v[1] is the other.
if v[0] > v[1]:
    (v[0], v[1]) = (v[1], v[0])

# Petya start with taking the color have single count if exists.
pre = 0 if v[0] % 2 == 1 else 1
cur = pre
v[cur] -= 1

# mov alters per step, to decide whether to flip.
# The second step is Vasya, he always filp if he can.
mov = 1


(a, b) = (0, 0)

while sum(v) > 0:
    
    # Filp by role.
    cur ^= mov

    # Take turns whether to filp.
    mov ^= 1

    # Flip back if not enough.
    if v[cur] == 0:
        cur ^= 1

    # Record the score.
    a += 1 if pre == cur else 0
    b += 0 if pre == cur else 1

    # Takes the cubes away.
    v[cur] -= 1

    # Remember the last.
    pre = cur

print('%d %d' % (a, b))
