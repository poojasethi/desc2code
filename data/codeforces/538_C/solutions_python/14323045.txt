__author__ = 'trunghieu11'


def solve(totalDays, n, info):
    answer = max(info[0][0] - 1 + info[0][1], totalDays - info[n - 1][0] + info[n - 1][1])
    for i in range(1, n):
        x = info[i - 1][1]
        y = info[i][1]
        height = info[i][0] - info[i - 1][0] - 1
        while height > 0 and x != y:
            diff = min(abs(x - y), height)
            if x >= y:
                y += diff
            else:
                x += diff
            height -= diff
        if height > 0:
            x += (height + 1) / 2
            y += height - (height + 1) / 2
        if abs(x - y) > 1:
            return "IMPOSSIBLE"
        else:
            answer = max(answer, x, y)
    return answer

if __name__ == '__main__':
    totalDays, n = map(int, raw_input().split(" "))
    info = []
    for i in range(n):
        info.append(map(int, raw_input().split(" ")))
    print solve(totalDays, n, info)