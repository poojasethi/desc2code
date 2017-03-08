__author__ = 'trunghieu11'

def solve(start, end, t, d):
    answer = start + end
    for i in range(t - 2):
        if start > end:
            end += d
            answer += end
        else:
            start += d
            answer += start
    return answer

if __name__ == '__main__':
    start, end = map(int, raw_input().split(" "))
    t, d = map(int, raw_input().split(" "))
    print solve(start, end, t, d)