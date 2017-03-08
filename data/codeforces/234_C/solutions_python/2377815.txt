import copy
import math
import sys

def solve(l_t):
    n = len(l_t)
    n_change = []
    should_plus = len([_ for _ in l_t[1:] if _<=0])
    should_minus = 0 if l_t[0]<0 else 1
    n_change_tmp = should_plus+should_minus
    n_change.append(n_change_tmp)

    for i in range(1, n-1):
        if l_t[i] == 0:
            pass
            #should_minus += 1
            #should_plus -= 1
        elif l_t[i] > 0:
            n_change_tmp += 1
        else: #l_t[i]<0:
            n_change_tmp -= 1
            n_change.append(n_change_tmp)



    return str(min(n_change))

def solve_old(l_t):
    n = len(l_t)
    ans = 0
    before = -1
    F_NEG, F_POS = False, False

    if l_t[0]==0:
        F_NEG = True
    if l_t[-1]==0:
        F_POS = True
    for i in range(n):
        tmp = l_t[i]
        if before < 0:
            if tmp == 0:
                ans+=1
            elif tmp >0:
                F_POS = True
                before = tmp
            else:
                F_NEG = True
                before = tmp

        elif before > 0:
            if tmp == 0:
                ans +=1
            elif tmp < 0:
                ans += 1
            else:
                F_POS = True
                before = tmp

    if not F_NEG and not F_POS:
        pass
    elif not F_NEG or not F_POS:
        ans += 1

    ans_pos = ans

    ans = 0
    F_NEG, F_POS = False, False
    before = 1

    if l_t[0]==0:
        F_NEG = True
    if l_t[-1]==0:
        F_POS = True
    for i in range(n-1, -1, -1):
        tmp = l_t[i]
        if before > 0:
            if tmp == 0:
                ans+=1
            elif tmp >0:
                F_POS = True
                before = tmp
            else:
                F_NEG = True
                before = tmp

        elif before < 0:
            if tmp == 0:
                ans +=1
            elif tmp > 0:
                ans += 1
            else:
                F_NEG = True
                before = tmp

    if not F_NEG and not F_POS:
        pass
    elif not F_NEG or not F_POS:
        ans += 1

    ans_neg = ans

    return str(min(ans_neg, ans_pos))



def test(ans, ll):
    tmp = solve([int(_) for _ in ll.split()])

    if tmp != str(ans):
        print 'WA, %s should %d : %s' % (tmp, ans, ll)
    else:
        print 'Correct! %d : %s' % (ans, ll)




if __name__ == '__main__':

    try:
        try:
            f_in = open(__file__[:-2]+"in")
            f_out = open(__file__[:-2]+"out", 'w')
        except IOError:
            f_in = open("input.txt")
            f_out = open("output.txt", 'w')
        FLAG_LOCAL = True

        n = int(f_in.next())
        l_t = [int(_) for _ in f_in.next().split()]

        output = solve( l_t)
        print output,

        if FLAG_LOCAL:
            f_out.write(output)
            f_in.close()
            f_out.close()

    except IOError:
        test(2, '0 0')
        test(3, '-1 0 0 0')
        test(4, '1 0 0 0')
        test(3, '0 -1 0 0')
        test(2, '0 -1 1 2 -5')
        test(2, '1 1 0 1')
        test(2, '1 1 0 1 1 1 1 1')
        test(4, '1 1 1 1 0 -1 -1')
        test(3, '0 1 1 1 0 -1 1')
        test(4, '1 1 0 -1 -1 -1 -1 -1 -1')
        test(4, '1 1 0 -1 -1 -1 -1 -1 0')
        test(4, '-1 1 -1 -1 1 -1 1 -1 1 -1 1')


        #f_in = sys.stdin
        FLAG_LOCAL = False

