__author__ = 'trunghieu11'


def solve(n, s):
    answer = 1
    cur = s[0]
    same = 0
    for i in range(1, n):
        answer += s[i] != cur
        cur = s[i]
        same += s[i] == s[i - 1]
    return answer + min(2, same)



if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input()
    print solve(n, s)