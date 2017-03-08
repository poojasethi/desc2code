__author__ = 'trunghieu11'

def main():
    t, s, q = map(int, raw_input().split())
    answer = 0
    while t > s:
        answer += 1
        s *= q

    print answer

if __name__ == '__main__':
    main()