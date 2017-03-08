__author__ = 'trunghieu11'

def main():
    n, query = map(int, raw_input().split())
    s = list(raw_input())

    answer = 0
    counter = 0
    for c in s:
        if c == '.':
            counter += 1
        else:
            answer += max(0, counter - 1)
            counter = 0
    answer += max(0, counter - 1)

    for i in range(query):
        line = raw_input().split()
        idx = int(line[0]) - 1
        c = line[1][0]
        if c == '.' and s[idx] != '.':
            answer += (idx - 1 >= 0 and s[idx - 1] == '.') + (idx + 1 < n and s[idx + 1] == '.')
        elif c != '.' and s[idx] == '.':
            answer -= (idx - 1 >= 0 and s[idx - 1] == '.') + (idx + 1 < n and s[idx + 1] == '.')
        s[idx] = c
        print answer

if __name__ == '__main__':
    main()